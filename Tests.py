from Journal_file import Journal



jour = Journal()

jour.add_student("John", [25, 45, 34])
jour.add_student("Mary", [30, 48])
jour.add_student("Alex", [28, 54, 32, 50])
jour.add_student("Sam", [46, 47, 31])


jour.get_all()


jour.update_mark("Alex", [34, 44])



print()
print(jour.get_mark("Alex"))

#print(" ".join(str(i) for i in jour.get_mark("Alex")))

