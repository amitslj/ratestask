# Import Python libraries
from flask import Flask, request, jsonify
import psycopg2

# Import file containing credentials for DB connection
import credentials


def get_db_conn():
    """
     description
        Method to create Postgres DB connection based on credentials
     returns
        DB connection string
    """
    try:
        connection = psycopg2.connect(
            user=credentials.connection.get('user'),
            password=credentials.connection.get('password'),
            host=credentials.connection.get('host')
        )
        return connection
    except Exception as err:
        print(err)


def get_data(query, args):
    """
     description
        This method will fetch rates from DB based on the input query and parameters
     returns
        prices data set
    """
    try:
        db_con = get_db_conn()
        cur = db_con.cursor()
        cur.execute(query, args)
        data = cur.fetchall()
        return data
    except Exception as err:
        print(err)


def convert_to_dict(rows):
    """
     description
        This method will convert the input prices to Python dictionary format
     returns
        prices in dictionary format
    """
    dict_price = []
    for day, avg_price in rows:
        price = {
            "day": day.isoformat(),
            "price": None if avg_price is None else str(avg_price)
        }
        dict_price.append(price)
    return dict_price


def get_custom_rates(origin, destination, date_from, date_to):
    """
     description
        This method comprises the SQL query to fetch the average rates
     returns
        average rates
    """
    rows = get_data(
        """
        with prices_cte as
        (
            select AVG(price) as price, day, count(*) as count
            from prices
            where 
            (orig_code = %(origin)s OR orig_code in (select code from ports where parent_slug = %(origin)s)) and
            (dest_code = %(destination)s OR dest_code in (select code from ports where parent_slug = %(destination)s)) and
            day >= %(date_from)s and 
            day <= %(date_to)s 
            GROUP BY day
        ),
        dates_cte as
        (
            select generate_series(%(date_from)s, %(date_to)s, '1 day'::interval) ::date as day
        )
        select 
        d.day as day,
        case when p.count < 3 then null else p.price end as average_price
        from dates_cte d
        left join prices_cte p on p.day=d.day
        """,
        {
            "origin": origin,
            "destination": destination,
            "date_from": date_from,
            "date_to": date_to
        }
    )

    final_price = convert_to_dict(rows)
    return final_price


def rates_app():
    """
     description
        This method will create the application which will display the rates based on parameters
     returns
        application to display rates data
    """
    app = Flask(__name__)

    @app.route("/")
    def welcome_rates_app():
        return jsonify({
            "HomePage": "Welcome To Rates Application"
        })

    @app.route("/rates", methods=["GET"])
    def get_rates():
        """
         description
            This method will fetch input parameters and pass on to the custom method to calculate prices
         returns
            average price per day
        """
        origin = request.args.get("origin")
        destination = request.args.get("destination")
        date_from = request.args.get("date_from")
        date_to = request.args.get("date_to")
        return get_custom_rates(origin, destination, date_from, date_to)

    return app


if __name__ == "__main__":
    app = rates_app()
    app.run(host="localhost", port=5000, debug=True)
