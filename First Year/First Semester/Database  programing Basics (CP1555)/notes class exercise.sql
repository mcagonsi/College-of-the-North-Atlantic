use ap;
 
select vendor_id , round(avg(invoice_total)) as avg_invoice_total 
from invoices
group by vendor_id
having avg(invoice_total) > 2000
order by vendor_id;

select vendor_name, vendor_state, round(avg(invoice_total),2) as invoice_average_amount
from invoices join vendors on invoices.vendor_id = vendors.vendor_id
group by vendor_name, vendor_name,terms_id
having avg(invoice_total) 
order by invoice_average_amount desc;

select  vendor_state, round(avg(invoice_total),2) as invoice_average_amount
from invoices join vendors on invoices.vendor_id = vendors.vendor_id
group by vendor_state
having avg(invoice_total) 
order by invoice_average_amount desc;

select vendor_id, count(*) as invoice_qty
from invoices 
group by vendor_id;

select vendor_state, vendor_city, count(*) as invoice_qty,
round(avg(invoice_total),2) as invoice_avg
from invoices join vendors
on invoices.vendor_id = vendors.vendor_id
group by vendor_state, vendor_city
order by vendor_state, vendor_city;