########  GENERAL APP INFORMATION  ##############

APP_TITLE = None
# APP_TITLE = "SC4x | Week 10 | Case Study | SQL 3"

APP_INTRO = None
# APP_INTRO = """The app uses an AI API (OpenAI, Gemini, or Claude) to evaluate and provide feedback on a SQL query to find the product category that has the highest average number of items in an order where the delivery was late for customers in either 'rio de janeiro' or 'sao paulo'."""

APP_HOW_IT_WORKS = None
# APP_HOW_IT_WORKS = """ """

SHARED_ASSET = {}
# SHARED_ASSET = {
#     "name":"NAME",
#     "path":"FILE.pdf",
#     "button_text":"Read this PDF first"
# }

HTML_BUTTON = {}

COMPLETION_MESSAGE = "Thank you for submitting a response!"
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = False

 ####### PHASES INFORMATION #########

PHASES = {
    "attempt1": {
        "type": "text_area",
        "height": 200,
        "label": """Write a query to find the product category that has the highest average number of items in an order where the delivery was late for customers in either 'rio de janeiro' or 'sao paulo'.""",
        "instructions": """ The students was asked to write a query to find the product category that has the highest average number of items in an order (average of item_qty) where the delivery was late (late_delivery=1) for customers in either 'rio de janeiro' or 'sao paulo'. One correct SQL query for this question:
                SELECT Products.product_category_name, AVG(OrderItems.item_qty)
                FROM Orders, OrderItems, Customers, Products
                WHERE Orders.order_id = OrderItems.order_id
                AND Customers.customer_id = Orders.customer_id
                AND OrderItems.product_id = Products.product_id
                AND Orders.late_delivery = 1
                AND (Customers.customer_city = 'rio de janeiro' OR Customers.customer_city = 'sao paulo')
                GROUP BY Products.product_category_name
                ORDER BY AVG(OrderItems.item_qty) DESC;
            There are variations to this query that will also give the correct result, such as using JOIN statements and the ROUND() function. Compare the following student submission with the correct answer above. Provide feedback on the student submission if their solution is not correct. Do not provide the correct answer. Instead, provide guidance to help the student identify where they might be missing something in their code. This is the student's first submission. They can follow up two more times. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
    "attempt2": {
        "type": "text_area",
        "height": 200,
        "label": """Do you want to try again?""",
        "instructions": """ The students was asked to write a query to find the product category that has the highest average number of items in an order (average of item_qty) where the delivery was late (late_delivery=1) for customers in either 'rio de janeiro' or 'sao paulo'. One correct SQL query for this question:
                SELECT Products.product_category_name, AVG(OrderItems.item_qty)
                FROM Orders, OrderItems, Customers, Products
                WHERE Orders.order_id = OrderItems.order_id
                AND Customers.customer_id = Orders.customer_id
                AND OrderItems.product_id = Products.product_id
                AND Orders.late_delivery = 1
                AND (Customers.customer_city = 'rio de janeiro' OR Customers.customer_city = 'sao paulo')
                GROUP BY Products.product_category_name
                ORDER BY AVG(OrderItems.item_qty) DESC;
            There are variations to this query that will also give the correct result, such as using JOIN statements and the ROUND() function. Compare the following student submission with the correct answer above. Provide feedback on the student submission if their solution is not correct. Do not provide the correct answer. Instead, provide guidance to help the student identify where they might be missing something in their code. This is the student's second submission. They can follow up one more time. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
    "attempt3": {
        "type": "text_area",
        "height": 200,
        "label": """Do you want to try one more time?""",
        "instructions": """ The students was asked to write a query to find the product category that has the highest average number of items in an order (average of item_qty) where the delivery was late (late_delivery=1) for customers in either 'rio de janeiro' or 'sao paulo'. One correct SQL query for this question:
                SELECT Products.product_category_name, AVG(OrderItems.item_qty)
                FROM Orders, OrderItems, Customers, Products
                WHERE Orders.order_id = OrderItems.order_id
                AND Customers.customer_id = Orders.customer_id
                AND OrderItems.product_id = Products.product_id
                AND Orders.late_delivery = 1
                AND (Customers.customer_city = 'rio de janeiro' OR Customers.customer_city = 'sao paulo')
                GROUP BY Products.product_category_name
                ORDER BY AVG(OrderItems.item_qty) DESC;
            There are variations to this query that will also give the correct result, such as using JOIN statements and the ROUND() function. Compare the following student submission with the correct answer above. Provide feedback on the student submission if their solution is not correct. Do not provide the correct answer. Instead, provide guidance to help the student identify where they might be missing something in their code. This is the student's last submission. They can't ask again. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
}

######## AI CONFIGURATION #############

########## AI ASSISTANT CONFIGURATION #######
ASSISTANT_NAME = "sc4x_wk10_CaseStudy_SQL"
ASSISTANT_INSTRUCTIONS = """ You are an expert in SQL and the instructor of a course where students are learning the basics of SQL. """

LLM_CONFIGURATION = {
    "gpt-4-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4-turbo",
        "temperature":0,
        "price_per_1k_prompt_tokens":.01,
        "price_per_1k_completion_tokens": .03
    },
    "gpt-4o":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4o",
        "temperature":0,
        "price_per_1k_prompt_tokens":.0025,
        "price_per_1k_completion_tokens": .010
    },
    "gpt-3.5-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-3.5-turbo-0125",
        "temperature":0,
        "price_per_1k_prompt_tokens":0.0005,
        "price_per_1k_completion_tokens": 0.0015
    }
}

ASSISTANT_THREAD = ""
ASSISTANT_ID_FILE = "assistant_id.txt"