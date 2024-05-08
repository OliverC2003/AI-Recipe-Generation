import re

Example_text = """
Bacon, Egg, and Cheese Bagel:
### Ingredients:
- 2 bagels, halved
- 4 slices of bacon
- 4 eggs
- 1 cup shredded cheese (cheddar or your preferred type)
- Butter or oil for cooking
- Salt and pepper to taste

### Instructions:
1. **Cook the Bacon:**
   - In a skillet over medium heat, cook the bacon until crispy. Remove from the skillet and place on paper towels to drain the excess fat. Break the bacon slices in half once cooled.

2. **Prepare the Eggs:**
   - In the same skillet, reduce heat to medium-low and add a little butter or oil if needed.
   - Crack the eggs into the skillet. For a neat fit on the bagel, you can cook them one at a time using a round cookie cutter as a mold in the skillet.
   - Sprinkle salt and pepper over the eggs as they cook. Flip them after about 2 minutes or once the bottom is set and cook to your preferred doneness.

3. **Toast the Bagels:**
   - While the eggs are cooking, toast your bagel halves until they are nicely browned and crispy.

4. **Assemble the Sandwich:**
   - Place the bottom halves of the toasted bagels on plates.
   - Layer each with a scoop of shredded cheese immediately so the heat melts it.
   - Place a cooked egg on top of the cheese on each bagel half.
   - Add two halves of bacon on top of the egg.
   - If you like, you can add another sprinkle of cheese on top of the bacon before covering with the top half of the bagel.

5. **Serve Hot:**
   - Serve your bacon, egg, and cheese bagel sandwiches hot for a satisfying and filling breakfast.

This sandwich is customizable with additional ingredients like sliced tomatoes, avocados, or a spread of cream cheese on the bagel for extra flavor.
"""

def process_ingredients(ingredients_text):
    lines = ingredients_text.split('\n')
    ingredients = []
    
    # Iterate over each line
    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        # Extract the ingredient item
        ingredient = line.replace('-', '').strip()
        # Append the ingredient to the list
        ingredients.append(ingredient)
    
    return ingredients

def process_instructions(instructions_text):
    # Use a regex pattern that matches numbers followed by a dot and space
    pattern = r"(\d+\.\s)"
    
    # Find all matches for the pattern
    matches = list(re.finditer(pattern, instructions_text))
    
    # Extract the instructions using the matches
    instructions = []
    for i, match in enumerate(matches):
        start_idx = match.start()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(instructions_text)
        instructions.append(instructions_text[start_idx:end_idx].strip())

    return instructions

def process_whole_text(text):
    # Split the text into parts using headers "### Ingredients:" and "### Instructions:"
    parts = re.split(r"###\s+(Ingredients:|Instructions:)", text)
    item = parts[0].strip().rstrip(':')
    item = item.replace('Name Of dish:', '').strip()

    ingredients_text = ""
    instructions_text = ""
    
    # Process parts
    for i in range(1, len(parts), 2):
        if parts[i].strip() == "Ingredients:":
            ingredients_text = parts[i + 1].strip()
        elif parts[i].strip() == "Instructions:":
            instructions_text = parts[i + 1].strip()

    # Process the ingredients and instructions using the provided functions
    ingredients = process_ingredients(ingredients_text)
    instructions = process_instructions(instructions_text)
    
    return item, ingredients, instructions

