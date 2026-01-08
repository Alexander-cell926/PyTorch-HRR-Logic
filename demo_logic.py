import torch
from hrr_core import HRR

def main():
    print("========================================")
    print("   🔮 ARTIFACT #3: THE LOGIC ENGINE")
    print("========================================")
    
    # 1. SETUP
    # HRRs need high dimensions (e.g., 1024 or 2048) to work cleanly due to noise
    hrr = HRR(dim=2048) 
    
    # 2. CREATE BASE CONCEPTS
    print("\n[1] Creating Base Concepts...")
    # Attributes
    color = hrr.create_concept("Color")
    shape = hrr.create_concept("Shape")
    taste = hrr.create_concept("Taste")
    
    # Values
    red = hrr.create_concept("Red")
    round_shape = hrr.create_concept("Round")
    sweet = hrr.create_concept("Sweet")
    
    # Objects
    apple_id = hrr.create_concept("Apple_ID")
    
    print("    Created vectors for: Color, Shape, Red, Round, Apple...")

    # 3. BUILD A COMPLEX OBJECT
    print("\n[2] Binding Concepts to create an 'Apple'...")
    # Formula: Apple = (Color * Red) + (Shape * Round) + (Taste * Sweet)
    # We "Bind" Key+Value, then "Superpose" (Add) them together.
    
    feat1 = hrr.bind(color, red)       # "Color is Red"
    feat2 = hrr.bind(shape, round_shape) # "Shape is Round"
    feat3 = hrr.bind(taste, sweet)     # "Taste is Sweet"
    
    # Superposition (Adding vectors bundles them into one object)
    apple_object = feat1 + feat2 + feat3
    
    print("    'Apple' is now a single vector containing 3 facts.")

    # 4. QUERY THE OBJECT
    print("\n[3] Solving Logic Puzzle: 'What is the Color of the Apple?'")
    # Algebra: Answer = Apple_Object (-) Color
    # We use the 'unbind' operation to subtract the "Color" key.
    
    answer_vec = hrr.unbind(apple_object, color)
    
    # 5. CHECK RESULT
    # The result is a noisy vector. We compare it against all known concepts to find the match.
    # This is like "Cleaning up" the memory.
    
    print("    Comparing result against known concepts...")
    
    # List of candidate answers
    vocabulary = {
        "Red": red,
        "Round": round_shape,
        "Sweet": sweet,
        "Color": color, # Should not be this
        "Apple": apple_object
    }
    
    best_match = None
    highest_score = -1.0
    
    for name, vec in vocabulary.items():
        score = hrr.similarity(answer_vec, vec)
        print(f"    Similarity to '{name}': {score:.4f}")
        
        if score > highest_score:
            highest_score = score
            best_match = name
            
    print(f"\n✅ THE LOGIC ENGINE SAYS: The Color of the Apple is **{best_match.upper()}**")

if __name__ == "__main__":
    main()
