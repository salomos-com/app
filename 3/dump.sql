SELECT *
FROM Customers
WHERE CustomerID IN (
    SELECT CustomerID
    FROM Orders
    WHERE OrderDate >= DATEADD(month, -1, GETDATE())
);