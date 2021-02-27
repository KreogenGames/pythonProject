def f23(x):
    final = []
    emptyLine = 0

    for i in range(0, len(x)): # Цикл узнает, сколько пустых строк в таблице
            for elem in x[i]:
                if elem == None:
                    emptyLine += 1
                    break

    for i in range(0, emptyLine): # Цикл бежит от 0 до количества пустых строк, и удаляет все из них
        check = 0
        for j in range(0, len(x)):
            for elem in x[j]:
                if elem == None:
                    del x[j]
                    check = 1
                    break
            if check == 1:
                break

    for i in x:  # Цикл избавляется от дубликатов и получает массив final
        if i not in final:
            final.append(i)

    for i in range(0, len(final)):
        chislo = final[i][0][:-1] # Присваиваем переменной chislo нашу строку без знака процентов
        chislo = int(chislo)      # Превращаем переменную типа string в тип float
        if chislo // 10 == 0:      # Если число однозначное
            if 0 <= chislo <= 5:  # Если это число от 0 до 5, то округляем и делаем число равным 0
                chislo = 0
            else:                 # Иначе же делаем ее равной 10, то есть округяем в большую сторону
                chislo = 10
        if chislo // 10 != 0:      # Если число не однозначное
            if chislo == 45:      # Делаем исключение для 45 и округляем его в большую сторону, превращая в 50
                chislo = 50
            else:                 # Если же это не 45
                if chislo % 10 > 5:     # Если последняя цифра числа больше пяти
                    chislo = chislo // 10 # То отрубай последнее число, прибавляй и и умножай на десять (тем самым мы округлям в БОЛЬШУЮ сторону)
                    chislo += 1
                    chislo = chislo * 10
                else:                    # Иначе же
                    chislo = chislo // 10 # Просто отрубай последнее число и умножай на десять (тем самым мы округляем в МЕНЬШУЮ сторону)
                    chislo = chislo * 10
        if chislo // 10 == 0:     # Опять делаем проверку, какое у нас число. Если это однознчное
            chislo = str(chislo)  # То сразу превращаем ее в тип string и вставляем обратно в таблицу
            final[i][0] = chislo
        else:                     # Если же это число не однозначное, то мы делим его на 100, превращаем в тип string и кладем обратно в таблицу
            chislo = chislo / 100
            chislo = str(chislo)
            final[i][0] = chislo
        ready = ""               # Теперь начинаем работать с почтой. В переменной ready будет лежать все, что находится до "[at]"
        for k in range(0, len(final[i][2])): # Циклом бежим по строке типа "blabla[at]mail.ru"
            if final[i][2][k] != "[":      # Если это не символь "[", то добавляем элемент в ready
                ready += final[i][2][k]
            else:                        # Иначе же прерываем нам цикл, так как дальше бежать нам уже смысла нет
                break
        final[i].append(ready)           # Добавляем наше ready в конец строки - как раз туда, куда нам и нужно. Этим же действием мы делаем превращаем длину строки из 3ки в 4ку (Добавили же элемент туда, логично)
        if "true" in final[i][1]:        # Теперь приступаем к третьему столбцу, то есть там, где у нас Да/Нет. Если мы находим "true" в строчке с телефоном
            final[i][2] = "Да"           # То в третий столбец пишем "Да"
        else:                            # Иначе же пишем "Нет"
            final[i][2] = "Нет"
        final[i][1] = final[i][1][7:13] + final[i][1][14:16] # Теперь работам с номером телефона. Мы отрезаем нужный нам кусок с 7 по 16 индексы и вставляем его обратно на место в таблицу
    final.sort(key = lambda i: i[3])    # Сортируем массив по четвертому столбцу
    return final

print(f23([["14%", "+7(454)415-08-47:true", "sebeduk35[at]yahoo.com"], ["15%", "+7(038)142-30-27:true", "dasomij76[at]rambler.ru"], ["15%", "+7(038)142-30-27:true", "dasomij76[at]rambler.ru"], [None, None, None], ["15%", "+7(038)142-30-27:true", "dasomij76[at]rambler.ru"], ["79%", "+7(037)610-74-99:true", "lavin61[at]yandex.ru"]]))
print(f23([["45%", "+7(188)891-42-53:false", "muvicov99[at]rambler.ru"], ["21%", "+7(477)452-81-82:true", "zirov16[at]rambler.ru"], [None, None, None], ["21%", "+7(477)452-81-82:true", "zirov16[at]rambler.ru"], ["21%", "+7(477)452-81-82:true", "zirov16[at]rambler.ru"], ["8%", "+7(511)347-80-16:false", "kamilman19[at]mail.ru"], ["95%", "+7(128)007-91-15:false", "todedic73[at]yahoo.com"]]))