# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()


    # Implement here your logic...

    path_fackturama = r"C:\Users\sabri\Documents\Fakturama2\Fakturama.exe"

    bot.execute(path_fackturama)

    bot.wait(5000)


    # Criando alerta
    maestro.alert(
    task_id=execution.task_id,
    title="Alerta de Informação",
    message="Cadastro de produtos sendo realizado",
    alert_type=AlertType.INFO
    )


   # Lista de produtos
    produtos = [
        {
            "Item Number": 1,
            "Name": "Laptop",
            "Category": "Eletrônico",
            "GTIN": "1234567890123",
            "Supplier Code": "SUP001",
            "Description": "Alto desempenho com as últimas especificações.",
            "Price": 999.99,
            "Cost Price": 799.99,
            "Allowance": 50,
            "Stock": 100
        },
        {
            "Item Number": 2,
            "Name": "Smartphone",
            "Category": "Eletrônico",
            "GTIN": "9876543210987",
            "Supplier Code": "SUP002",
            "Description": "Smartphone com recursos avançados de câmera e display.",
            "Price": 699.99,
            "Cost Price": 549.99,
            "Allowance": 30,
            "Stock": 150
        },
        {
            "Item Number": 3,
            "Name": "Tenis de corrida",
            "Category": "Esporte",
            "GTIN": "7654321098765",
            "Supplier Code": "SUP003",
            "Description": "Confortável e resistente, ideal para corridas.",
            "Price": 89.99,
            "Cost Price": 69.99,
            "Allowance": 20,
            "Stock": 200
        }
    ]
    

    for produto in produtos:
        # Searching for element 'new_product'
        if not bot.find("new_product", matching=0.97, waiting_time=10000):
            not_found("new_product")
        bot.click()
        
        # Searching for element 'item_number'
        if not bot.find("item_number", matching=0.97, waiting_time=10000):
            not_found("item_number")
        bot.click_relative(98, 10)
        
        bot.paste(produto["Item Number"])

        bot.tab()
        bot.kb_type(produto["Name"])

        bot.tab()
        bot.paste(produto["Category"])

        bot.tab()
        bot.paste(produto["GTIN"])

        bot.tab()
        bot.paste(produto["Supplier Code"])

        bot.tab()
        bot.paste(produto["Description"])

        bot.tab()
        bot.control_a()
        bot.paste(produto["Price"])

        bot.tab()
        bot.control_a()
        bot.paste(produto["Cost Price"])

        bot.tab()
        bot.paste(produto["Allowance"])

        bot.tab()
        bot.tab()
        bot.control_a()
        bot.paste(produto["Stock"])

        bot.control_s()

        bot.control_w()

    bot.alt_f4()

    # Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK.",
        total_items=0,
        processed_items=0,
        failed_items=0
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()