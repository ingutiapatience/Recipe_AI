from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Configuration
openai.api_key = "your_openai_api_key"  # Replace with your actual API key

@app.route('/')
def index():
    return render_template('index.html')  # The HTML frontend file

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    ingredients = request.form.get('ingredients')
    if not ingredients:
        return jsonify({"error": "Please provide some ingredients!"}), 400

    try:
        # Generate recipe using OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a detailed recipe using these ingredients: {ingredients}",
            max_tokens=300,
            temperature=0.7
        )
        recipe = response.choices[0].text.strip()
        return jsonify({"recipe": recipe})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
