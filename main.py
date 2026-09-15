import os
print("===================================")
print("  JARVIS AI Assistant Initializing...")
print("===================================")

def main():
    # ভবিষ্যতে এখানে জেমিনি বা গ্রোক এপিআই এবং ভয়েস কমান্ড যুক্ত হবে
    assistant_name = "Jarvis"
    print(f"Hello! I am your personal assistant, {assistant_name}.")
    
    user_input = input("Type a command for Jarvis (or type 'exit'): ")
    
    if user_input.lower() == 'exit':
        print("Shutting down Jarvis. Goodbye!")
    else:
        print(f"You said: {user_input}")

if __name__ == "__main__":
    main()
