class Animal:
    def __init__(self, name):
        self.name = name

    # raiseは例外を発生させるコード(今回はエラー)
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"


"""
DogクラスはAnimalクラスから継承されており、
Dogクラスのインスタンスを作成するときには、
nameとbreedという2つの引数を取ります。
Dogクラスは、speak()メソッドを実装していますが、
Animalクラスのspeak()メソッドは実装されていません。
Animalクラスのspeak()メソッドは、抽象メソッドとして定義されており、
Dogクラスでは実装する必要があります。

super()は、親クラスのメソッドを呼び出すために使用されます。
Dogクラスの__init__メソッドでは、super().__init__(name)という形式で、
Animalクラスの__init__メソッドを呼び出しています。
これにより、name属性が設定されます。
"""