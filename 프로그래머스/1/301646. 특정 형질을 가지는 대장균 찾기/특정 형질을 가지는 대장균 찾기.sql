select count(*) as COUNT
from ECOLI_DATA
where GENOTYPE  & b'0010' != b'0010' and (GENOTYPE  & b'0100' = b'0100'  or GENOTYPE  & b'0001' = b'0001' )
