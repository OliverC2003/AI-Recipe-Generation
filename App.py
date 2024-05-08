from flask import Flask, render_template, request, session, jsonify
import generate as gen
import generate_langchain_variant as genlang

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_here'

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredients_text = request.form['ingredients']  
        response = genlang.generate_message(ingredients_text)
        response = gen.prep.process_whole_text(response)
        
        data = []
        
        item_of_food, ingredients, instructions = response
        
        item_of_food_image_url = gen.generate_image(item_of_food)

        data.append((item_of_food, item_of_food_image_url))

        ingredients_image_url = gen.generate_image(str(ingredients))
        ingredients = ' '.join(str(x) for x in ingredients)

        data.append((ingredients, ingredients_image_url))
        
        for instruction in instructions:
            instruction_image_url = gen.generate_image(instruction)
            data.append((instruction, instruction_image_url))

        session['data'] = data
        session['index'] = 0
        return render_template("home.html")

    return render_template("home.html")

@app.route("/get-next")
def get_next():
    index = session.get('index', 0)
    data = session.get('data', [])

    text = "Let's cook something up"
    image_url = "https://png.pngtree.com/png-clipart/20230218/original/pngtree-cartoon-chef-with-a-confident-pose-png-image_8958326.png"

    if index < len(data):
        text, image_url = data[index]
        session['index'] = index + 1  

    return jsonify({'text': text, 'image_url': image_url})
    
if __name__ == "__main__":
    app.run(debug=True)

