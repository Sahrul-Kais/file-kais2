CREATE TABLE "Product" (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name" TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	"id_category" INTEGER NOT NULL,
	"id_cashier" INTEGER NOT NULL
);

INSERT INTO Product
(name,price,id_category,id_cashier)
VALUES('Latte',10000,2,1),
      ('Cake',20000,1,2),
      ('Mie',45000,1,3)
	   
SELECT * FROM Product

CREATE TABLE "Category" (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name" TEXT NOT NULL
);

INSERT INTO Category
(name)
VALUES('Food'),
      ('Drink')

SELECT * FROM Category

CREATE TABLE "Cashier" (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name" TEXT NOT NULL
);

INSERT INTO Cashier
(name)
VALUES('Pevita Pearce'),
      ('Raisa Andriana'),
      ('Sahrul Kais')

SELECT * FROM Cashier

SELECT
	Cashier.name AS cashier,
	Product.name AS product,
	Category.name AS category,
	Product.price AS price
FROM Product
LEFT JOIN Cashier ON Cashier.id = Product.id_cashier
LEFT JOIN Category ON Category.id = Product.id_category