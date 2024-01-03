def simplify_path(path):
    print(path.split("/"))
    stack = []
    for i in path.split("/"):
        if i == "..":
            if stack:
                stack.pop()
        elif i == "." or i == "":
            continue
        else:
            stack.append(i)
            
    return "/" + "/".join(stack)
    
print(simplify_path("/../"))