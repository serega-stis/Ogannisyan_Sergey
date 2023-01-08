from stats import *

data: List[Vacancy] = csv_filer(*csv_reader('vacancies_dif_currencies.csv'))

new_vac = None
old_vac= None


for vacancy in data:
	if not old_vac:
		old_vac = vacancy
	if not new_vac:
		new_vac = vacancy
	if vacancy.published_at < old_vac.published_at:
		old_vac = vacancy
	if vacancy.published_at > new_vac.published_at:
		new_vac = vacancy

print(f'Дата публикации самой старой вакансии: {old_vac.published_at}\nДата публикации самой новой вакансии: {new_vac.published_at}')
