import pandas as pd
import pyperclip

def main():
    df = pd.read_csv('data/제주특별자치도_서귀포시_고령화비율및노령화지수현황_20250421.csv', encoding = 'cp949')
    df.to_csv('data/제주특별자치도_서귀포시_고령화비율및노령화지수현황_20250421_utf-8.csv', encoding = 'utf-8', index = False)
    pyperclip.copy('제주특별자치도_서귀포시_고령화비율및노령화지수현황_20250421_utf-8.csv')

if __name__ == '__main__':
    main()