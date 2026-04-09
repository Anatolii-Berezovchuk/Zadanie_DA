-- №1 Абитуриенты
SELECT
  id,
  scores,
  DENSE_RANK() OVER (ORDER BY scores DESC) AS position -- одинаковые баллы получают одинаковую позицию, без пропусков в нумерации.
FROM examination;

-- №2 FULL JOIN
Ответ Минимально 30 и максимально 50 строк.

-- №3 Покупки
SELECT
  a.client_id
FROM account a
LEFT JOIN transaction t
  ON t.account_id = a.id
  AND t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
  AND t.type = 'PUR' -- оставляем в соединении только транзакции типа покупка (purchase).
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000 OR SUM(t.amount) IS NULL
