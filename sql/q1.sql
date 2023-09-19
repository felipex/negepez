--select concat('*', nome_servidor, '*') from dw_servidores limit 3;
--select concat('*', trim(nome_servidor), '*') from dw_servidores limit 3;
drop view vw_servidores;
create view vw_servidores as
select *,
case 
when cargo like 'PROFESSOR%' then 'PROFESSOR'
when cargo like 'S/cargo' then situacao_vinculo
else 'TAE'
end as categoria
 from dw_servidores
left join dw_uo_siorg on codigo = trim(cod_siorg_uorg);


