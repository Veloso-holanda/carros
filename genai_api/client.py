from google import genai


def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo
    '''
    client = genai.Client(api_key="AIzaSyCzeJmW43jSN-HFZ6zenYb8FE7qbXKQ-n8")
    prompt = prompt.format(brand, model, year)
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt,
    )
    return response.candidates[0].content.parts[0].text

