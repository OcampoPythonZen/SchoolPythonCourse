import logging

class CramerMethod(object):

    def filter_system_expresion(self, system='') -> list:
        sub_matrix = []
        for e in system:
            try:
                e = int(e)
                sub_matrix.append(e)
            except ValueError as e:
                logging.info('Error: {}'.format(e))
        return sub_matrix

    def representation_complete_matrix(self,
                                       sub_matrix: list,
                                       sub_matrix_two: list,
                                       sub_matrix_three: list) -> list:
        complete_matrix = []
        complete_matrix.append(sub_matrix)
        complete_matrix.append(sub_matrix_two)
        complete_matrix.append(sub_matrix_three)
        return complete_matrix


if __name__ == "__main__":
    logging.basicConfig(
        format='Date-time: %(asctime)s : Line No. : %(lineno)d - %(message)s', level=logging.DEBUG)
    co = CramerMethod()
    x = co.filter_system_expresion('3X+2Y+1Z')
    y = co.filter_system_expresion('2x+0y+1z')
    z = co.filter_system_expresion('-1x+1y+2z')
    logging.info('Complete Systems Matrix: {}'.format(
        co.representation_complete_matrix(x, y, z)))
