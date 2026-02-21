# In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower(). Do not use Counter collection.
 
text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."
text= text.lower()
remove = ",. -"
table = str.maketrans("","",remove)
new_str=text.translate(table)
count={}
for val in new_str:
    if(val not in count):
        count[val]=1
    else:
        count[val]+=1
print(count)