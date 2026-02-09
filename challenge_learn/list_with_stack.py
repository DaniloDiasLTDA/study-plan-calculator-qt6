

card_stack = []

card_stack.append("Ace")
card_stack.append("Jack")
card_stack.append("Queen")

top_card = card_stack.pop()
print(top_card)

top_card = card_stack[-1]
print(top_card)

if not card_stack:
    print("Stack is empty")
else:
    print(len(card_stack))
