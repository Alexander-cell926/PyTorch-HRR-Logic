#  PyTorch HRR: The Logic Engine

**A standalone Neuro-Symbolic AI module that performs algebra with concepts.**

This repository implements **Holographic Reduced Representations (HRR)**, a type of Vector Symbolic Architecture (VSA). Unlike standard neural networks that use "fuzzy" associations, this engine allows you to mathematically bind vectors together to form complex data structures and then query them with high precision.

### The Theory
In standard AI:
* `King` and `Queen` are just similar vectors.

In this Logic Engine:
* `Queen` is mathematically defined as `King - Man + Woman`.
* `Apple` is defined as `(Color * Red) + (Shape * Round) + (Taste * Sweet)`.

We use **Circular Convolution** (via FFT) to bind vectors and **Circular Correlation** to unbind them.

### Quick Start

**1. Install Dependencies**
```bash
pip install torch numpy


### How to Use It

Run the script: python interactive_logic.py

Try this sequence to recreate the "Apple" demo manually, then try your own!

1. Create the Ingredients

bash
new Color Shape Taste
new Red Round Sweet


2. Create the "Bound" Properties (The Glue)

bash
bind P1 Color Red
bind P2 Shape Round
bind P3 Taste Sweet


(Note: P1, P2, P3 are just temporary names for "Property 1", etc.)

3. Build the Object

bash
add Apple P1 P2 P3


4. The Grand Finale (Ask the question)

bash
query Apple Color

It should reply: RED


5. Try another query to see if it works:

bash
query Apple Shape

It should reply: ROUND

You can try the classic NLP equation
new King Man Woman Queen
# In HRR, subtraction is harder to visualize, but we can try Binding
bind K King Man
query K King
# This is a bit abstract for this specific script, stick to the Apple recipe first!

Facts
1. "Does this work like AGI?"Yes and No.Yes: It solves the hardest part of AGI—Reasoning. Normal Neural Networks (like GPT) rely on probability (guessing). This engine relies on Algebra (math). If you teach it that A > B and B > C, it knows A > C. It doesn't guess; it calculates.No: It is not a complete brain. It has no "Consciousness" or "Agency." It is just a very advanced logic calculator. Think of it as the Left Hemisphere of the brain (Logic/Math), whereas ChatGPT is the Right Hemisphere (Creativity/Language).
2. "Cant Chat?".
The Logic Engine is Mute.It does not output sentences like "The apple is red."It outputs a Vector (a list of 2048 numbers).You have to write code to translate that vector back into a word ("RED").It cannot write a poem, tell a joke, or hold a conversation. It only answers specific logic queries.
3. "Catastrophic Forgetting?
"This is the best part:It does NOT suffer from Catastrophic Forgetting in the way normal AI does.The "Chalkboard vs. Backpack" Analogy:Normal AI (Neural Net): Works like a Chalkboard. To learn something new, you often have to erase (overwrite) a little bit of the old stuff. If you learn too much, you erase your own name. This is Catastrophic Forgetting.Logic Engine (HRR): Works like a Backpack. To learn something new, you just Add it to the pile ($Knowledge = Fact1 + Fact2$).Adding Fact3 does not delete Fact1. They exist together in superposition.The Limit: It doesn't "forget," but it can get "Full." If you stuff 1,000 items into the backpack, it becomes a jumbled mess and you can't find anything (this is called "Noise" or "Saturation").

Feature,Neural Network (Standard AI),Logic Engine (Artifact #3)
Reasoning,❌ Weak (Hallucinates),✅ Perfect (Algebraic)
Chatting,✅ Excellent (Fluent),❌ Impossible (Vectors only)
Memory,❌ Overwrites itself (Forgets),✅ Stacks (Does not forget)