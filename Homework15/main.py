import argparse
import logging
from students import Student, StudentNameError, InvalidSubjectError, InvalidScoreError

logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)
        # Вызываем ошибку класса Student
        student.add_score('Математика', 6)

    except StudentNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e.message}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e.message}')


if __name__ == '__main__':
    main()


