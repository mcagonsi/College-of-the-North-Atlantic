use ap;

-- Question 1
/*What is the terms type that has the largest number of invoices, 
and how many invoices are there? */
select terms_description, count(*) as number_of_invoices
from invoices join terms on invoices.terms_id = terms.terms_id
group by terms_description
order by number_of_invoices desc
limit 1;
-- ANSWER: the Net due 30 days has the largest number of invoices with 80 in total

-- Question 2
/*Show the number of invoices payments per months */
select monthname(payment_date) as month_name, count(*) as number_of_invoices
from invoices
where monthname(payment_date) is not null -- This line is optional, i figured it would take out the null values.
group by month_name
order by number_of_invoices
;

-- Question 3
/* For the general ledger accounts that have line items that sum to more than $10,000  show the general ledger account, 
the number of items and the total of those items, sorted by descending order of the total. */
select account_description  as 'General Ledger Account', count(*) as 'Number of Items', sum(line_item_amount) as total_amount_of_line_items
from invoice_line_items join general_ledger_accounts on invoice_line_items.account_number = general_ledger_accounts.account_number
group by account_description
having total_amount_of_line_items > 10000
order by total_amount_of_line_items desc
;


