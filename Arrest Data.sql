--For this SQL project i will be answering 6 question from this data set
--Let start by introducing the table 


SELECT 
	*
FROM 
	Arrest_Data$;

-- 1. What percentage of the total reports do "BOOKING" and "RFC" represent?
SELECT 
	[Report Type],
    COUNT(*) AS Report_Count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS Percentage_Total
FROM 
	Arrest_Data$
GROUP BY
	[Report Type];


-- 2. What is the average age in the dataset?

SELECT 
	AVG([Age]) AS Avg_Age
FROM 
	Arrest_Data$;


-- 3. What is the most frequently occurring city in the dataset,and how many times does it appear? 

SELECT 
	[Area Name], COUNT(*) AS City_Occurences
FROM 
	Arrest_Data$
GROUP BY 
	[Area Name]
ORDER BY 
	City_Occurences ASC;


-- 4. Which City has the highest count of females and Male arrest?

SELECT
    [Area Name],
    [Sex Code],
    Gender_Per_City_Count
FROM (
    SELECT
        [Area Name],
        [Sex Code],
        COUNT(*) AS Gender_Per_City_Count,
        ROW_NUMBER() OVER (PARTITION BY [Sex Code] ORDER BY COUNT(*) DESC) AS RowNum
    FROM 
        Arrest_Data$
    WHERE 
        [Area Name] IS NOT NULL AND [Sex Code] IS NOT NULL
    GROUP BY 
        [Area Name], [Sex Code]
) RankedData
WHERE
    RowNum <= 3;


-- 5. How many arrests occurred for each month and year in the dataset?

SELECT
    DATENAME(MONTH, [Arrest Date]) AS Arrest_Month,
    YEAR([Arrest Date]) AS Arrest_Year,
    COUNT(*) AS Arrest_Count
FROM
    Arrest_Data$
GROUP BY
    DATENAME(MONTH, [Arrest Date]),
    YEAR([Arrest Date])
ORDER BY 
    Arrest_Year ASC, Arrest_Count ASC;


-- 6. What is the average time taken for arrests and the most common charge description in each area?

SELECT
    [Area Name],
    FORMAT(CAST(AVG([Time]) AS DATETIME), 'hh:mm tt') AS AverageTime,
    MAX([Charge Description]) AS CommonChargeDescription
FROM
    Arrest_Data$
GROUP BY
    [Area Name]
ORDER BY
    [Area Name];
