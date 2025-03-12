languages = ['python', 'django', 'html', 'css', 'javascritp']


stack_dev_1 = ['python', 'django', 'html', 'css', 'javascritp']
stack_dev_2 = ['php', 'laravel', 'html', 'css', 'javascritp']

count1 = 0
count2 = 0

for language in languages:
    if language in stack_dev_1:
        count1 += 1
    if language in stack_dev_2:
        count2 += 1


print(count1)
print(count2)

count3 = 0
count4 = 0

for language in languages:
    count3 += stack_dev_1.count(language)
    count4 += stack_dev_2.count(language)


print(count3)
print(count4)

print(languages.count(stack_dev_1))