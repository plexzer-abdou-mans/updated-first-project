try:
    grade = 0
    dr = 0
    spt = 0
    pc = 0
    rel = 0
    cvl = 0
    hg = 0
    sy = 0
    phy = 0
    fr = 0
    eng = 0
    ar = 0
    math = 0
    p = 0
    print("---------------------------------------------------")
    print("arabic")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
            print("invalid number")
            print('re-insert')
            p = p + 1
     else:
        p = p + 1000
        print(str(x) , str(y) , str(z))
        ar = float(ar) + (x * 3) + y + z
        ar = float(ar) / 5
        print("arabic point :" + str(ar))
        ar = ar * 5

    print("---------------------------------------------------")
    print("math")
    p = p / 1000
    while p < 1000:
      x = float(input(" exam "))
      y = float(input(" test "))
      z = float(input(" evaliation "))
      if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print('re-insert')
        p = p + 1
      else:
        p = p + 1000
        print(x, y, z)
        math = float(math) + (x * 3) + y + z
        math = float(math) / 5
        print("math point :" + str(math))
        math = math * 4
    print("---------------------------------------------------")
    print("french")
    p = p / 1000
    while p < 1000:
      x = float(input(" exam "))
      y = float(input(" test "))
      z = float(input(" evaliation "))
      if x > 20 or y > 20 or z > 20:
          print("invalid number")
          print("re-insert")
          p = p + 1
      else:
        p= p + 1000
        print(x, y, z)
        fr = fr + (x * 3) + y + z
        fr = fr / 5
        print("french point :" + str(fr))
        fr = fr * 3
    print("---------------------------------------------------")
    print("english")
    p = p / 1000
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p + 1
     else:
        p = p + 1000
        print(x, y, z)
        eng = eng + (x * 3) + y + z
        eng = eng / 5
        print("english point" + str(eng))
        eng = eng * 2
    print("---------------------------------------------------")
    print("physiques")
    p = p / 1000
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p +1
     else:
      p = p+1000
      print(x, y, z)
      phy = phy + (x * 3) + y + z
      phy = phy / 5
      print("physiques point" + str(phy))
      phy = phy * 2
    print("---------------------------------------------------")
    print("science")
    p = p / 1000
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p + 1
     else:
        p = p + 1000
        print(x, y, z)
        sy = sy + (x * 3) + y + z
        sy = sy / 5
        print("science point" + str(sy))
        sy = sy * 2
    print("---------------------------------------------------")
    p = p / 1000
    print("history and geography")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p +1
     else:
        p = p + 1000
        print(x, y, z)
        hg = hg + (x * 3) + y + z
        hg = hg / 5
        print("history and geography point" + str(hg))
        hg = hg * 3
    print("---------------------------------------------------")
    p = p / 1000
    print("civil education")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p + 1
     else:
        p = p + 1000
        print(x, y, z)
        cvl = cvl + (x * 3) + y + z
        cvl = cvl / 5
        print("civil education point" + str(cvl))
    print("---------------------------------------------------")
    p = p / 1000
    print("religious education")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p +1
     else:
        p = p + 1000
        print(x, y, z)
        rel = rel + (x * 3) + y + z
        rel = rel / 5
        print("religious education point" + str(rel))
    print("---------------------------------------------------")
    p = p / 1000
    print("informatics")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        print("re-insert")
        p = p +1
     else:
        p = p + 1000
        print(x, y, z)
        pc = pc + (x * 3) + y + z
        pc = pc / 5
        print("informatics point" + str(pc))
    print("---------------------------------------------------")
    p = p / 1000
    print("sports")
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
     else:
        p = p + 1000
        print(x, y, z)
        spt = spt + (x * 3) + y + z
        spt = spt / 5
        print("sports point" + str(spt))
    print("---------------------------------------------------")
    print("draw")
    p = p / 1000
    while p < 1000:
     x = float(input(" exam "))
     y = float(input(" test "))
     z = float(input(" evaliation "))
     if x > 20 or y > 20 or z > 20:
        print("invalid number")
        p = p + 1
     else:
        p = p + 1000
        print(x, y, z)
        dr = dr + (x * 3) + y + z
        dr = dr / 5
        print("draw point" + str(dr))

    print("-----------------------------------------------------------------------")
    grade = grade + dr + spt + pc + rel + cvl + hg + sy + phy + fr + eng + ar + math
    grade = grade / 26
    if grade < 10:
         print("you failed " + str(grade))
    else:
      print("you succeeded " + str(grade))
except:
 print("error")
