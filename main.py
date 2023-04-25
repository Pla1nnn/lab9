def prog2():
    from PIL import Image, ImageFilter
    from pathlib import Path
    current = ''
    names = Path(current).glob('*')
    Path('photo').mkdir(parents=True, exist_ok=True)
    for file in names:
        if file.suffix in ['.jpg','.png']:
            with Image.open(file) as img:
                img.load()
                picture = img.filter(ImageFilter.CONTOUR)
                picture.save(Path("photo",file))


prog2()
def prog3():
    import csv
    file = open("text.csv","r")
    text = list(csv.reader(file, delimiter = ","))
    print("Купить:")
    for i in text:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1])*int(i[2]) for i in text])}руб.")
    file.close

prog3()