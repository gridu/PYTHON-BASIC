"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
import scraper


class Table:
    def __init__(self, title: str, column_names: list[str], data: list[list[str]]) -> None:
        self.title = title
        self.column_names = column_names
        self.data = data

    def _render_row(widths: list[int], data: list[str]) -> str:
        padded_data = [f' {s} ' for s in data]
        aligned_data = [f'{s : <{w+2}}' for w, s in zip(widths, padded_data)]
        return f'|{"|".join(aligned_data)}|'
    
    def __str__(self) -> str:
        result = ''
        widths = []
        for index, column in enumerate(self.column_names):
            max_width = max([len(row[index]) for row in self.data] + [len(column)])
            widths.append(max_width)
        total_width = len(Table._render_row(widths, self.column_names))
        result += f'{f'_{self.title.replace(' ', '_')}_' : ^{total_width}}'.replace(' ', '=').replace('_', ' ') + '\n'
        result += Table._render_row(widths, self.column_names) + '\n'
        for row in self.data:
            result += '-' * total_width + '\n'
            result += Table._render_row(widths, row) + '\n'
        result += '-' * total_width + '\n'
        return result


class Sheet1(Table):
    def __init__(self):
        self.title = '5 stocks with most youngest CEOs'
        self.column_names = ['Name', 'Code', 'Country', 'Employees', 'CEO Name', 'CEO Year Born']
        rows = scraper.get_sheet1_data()
        rows = sorted(rows, key=lambda row: row[-1], reverse=True)
        rows = rows[:5]
        self.data = rows


class Sheet2(Table):
    def __init__(self):
        self.title = '10 stocks with best 52-Week Change'
        self.column_names = ['Name', 'Code', '52-Week Change', 'Total Cash']
        rows = scraper.get_sheet2_data()
        rows = [r for r in rows if r[2] != '-']
        rows = sorted(rows, key=lambda row: float(row[2][:-1]), reverse=True)
        rows = rows[:10]
        self.data = rows


class Sheet3(Table):
    def __init__(self):
        self.title = '10 largest holds of Blackrock Inc.'
        self.column_names = ['Name', 'Code', 'Shares', 'Date Reported', '% Out', 'Value']
        rows = scraper.get_sheet3_data()
        rows = sorted(rows, key=lambda row: float(row[4][:-1]), reverse=True)
        rows = rows[:10]
        self.data = rows


def main():
    sheet1 = Sheet1()
    print(sheet1)
    sheet2 = Sheet2()
    print(sheet2)
    sheet3 = Sheet3()
    print(sheet3)


if __name__ == '__main__':
    main()
