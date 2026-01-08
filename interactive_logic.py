import torch
import shlex  # For parsing commands like a real terminal
from hrr_core import HRR
import sys

# Initialize the engine
DIMENSION = 2048
hrr = HRR(dim=DIMENSION)

# The "Knowledge Base" (Stores all vectors)
vocab = {}

def get_vec(name):
    """Helper to retrieve a vector or error if missing."""
    if name not in vocab:
        print(f"❌ Error: Concept '{name}' does not exist. Use 'new {name}' first.")
        return None
    return vocab[name]

def cmd_new(args):
    """Creates base concepts (random vectors). Usage: new [name]"""
    for name in args:
        if name in vocab:
            print(f"⚠️  Warning: '{name}' already exists. Skipping.")
        else:
            vocab[name] = hrr.create_concept(name)
            print(f"✨ Created concept: {name}")

def cmd_bind(args):
    """
    Binds two concepts into a new one. 
    Usage: bind [Result] [ConceptA] [ConceptB]
    Example: bind RedColor Color Red
    """
    if len(args) != 3:
        print("Usage: bind [ResultName] [Key] [Value]")
        return

    res_name, key_name, val_name = args
    vec_k = get_vec(key_name)
    vec_v = get_vec(val_name)
    
    if vec_k is not None and vec_v is not None:
        # Math: Result = Key * Value
        vocab[res_name] = hrr.bind(vec_k, vec_v)
        print(f"🔗 Bound '{key_name}' * '{val_name}' -> Created '{res_name}'")

def cmd_add(args):
    """
    Adds multiple bound concepts into a generic Object.
    Usage: add [ObjectName] [Part1] [Part2] ...
    Example: add Apple RedColor RoundShape SweetTaste
    """
    if len(args) < 2:
        print("Usage: add [ResultName] [Part1] [Part2] ...")
        return

    res_name = args[0]
    parts = args[1:]
    
    # Start with a zero vector
    composite = torch.zeros(DIMENSION)
    
    valid = True
    for part_name in parts:
        vec = get_vec(part_name)
        if vec is None:
            valid = False
            break
        composite += vec
        
    if valid:
        vocab[res_name] = composite
        print(f"📦 Combined {parts} -> Created Object '{res_name}'")

def cmd_query(args):
    """
    Solves for X.
    Usage: query [Object] [Key]
    Example: query Apple Color
    """
    if len(args) != 2:
        print("Usage: query [Object] [Key]")
        return

    obj_name, key_name = args
    vec_obj = get_vec(obj_name)
    vec_key = get_vec(key_name)
    
    if vec_obj is not None and vec_key is not None:
        print(f"🔍 Unbinding '{obj_name}' using key '{key_name}'...")
        
        # Math: Answer = Object (-) Key
        result_vec = hrr.unbind(vec_obj, vec_key)
        
        # Search Vocabulary for closest match
        best_match = "???"
        best_score = -1.0
        
        # Don't match against the query terms themselves to avoid confusion
        ignore = [obj_name, key_name]
        
        print(f"   [Top Matches]")
        for name, vec in vocab.items():
            if name in ignore: continue
            
            score = hrr.similarity(result_vec, vec)
            if score > 0.1: # Show relevant ones
                print(f"   - {name}: {score:.4f}")
            
            if score > best_score:
                best_score = score
                best_match = name
        
        print(f"\n✅ RESULT: The {key_name} of {obj_name} is **{best_match.upper()}**")

def main():
    print("==============================================")
    print("   🔮 LOGIC ENGINE INTERACTIVE SHELL (v1.0)")
    print("==============================================")
    print("Commands:")
    print("  new [name]          -> Create base concept (e.g., 'new Red')")
    print("  bind [res] [k] [v]  -> Bind Key+Val (e.g., 'bind RedColor Color Red')")
    print("  add [res] [a] [b]   -> Combine parts (e.g., 'add Apple RedColor...')")
    print("  query [obj] [key]   -> Ask a question (e.g., 'query Apple Color')")
    print("  list                -> Show all concepts")
    print("  exit                -> Quit")
    print("----------------------------------------------")

    while True:
        try:
            cmd_str = input("\nLogic> ").strip()
            if not cmd_str: continue
            if cmd_str.lower() in ["exit", "quit"]: break
            
            parts = shlex.split(cmd_str)
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd == "new": cmd_new(args)
            elif cmd == "bind": cmd_bind(args)
            elif cmd == "add": cmd_add(args)
            elif cmd == "query": cmd_query(args)
            elif cmd == "list": print(f"🧠 Memory: {list(vocab.keys())}")
            else: print("Unknown command.")
            
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()