# Simplex algorithm		  
# implemented by Lorena Leão

import numpy as np
import sys
import math
from fractions import Fraction
from operator import itemgetter

#duplicates the row indexed by "index" and places it bellow
def duplicate_row(numpy_array, index, num_dups):
 	return np.insert(numpy_array, (index+1)*num_dups, numpy_array[index], axis = 0)

#duplicates the column indexed by "index" and places it on the right
def duplicate_column(numpy_array, index, num_dups):
	return np.insert(numpy_array, (index+1)*num_dups, numpy_array[:, index], axis = 1)

def insert_identity_column(numpy_array, index1, signal, col_index):
	zeros = np.zeros_like(numpy_array)
	zeros[index1][col_index] = Fraction(1*signal)
	numpy_array = np.insert(numpy_array, col_index+1, zeros[:, col_index], axis = 1)
	return numpy_array

def create_FPI_tableau(numberOfVariables, nonNegativity, symbols, matrix_constraints, objFunction, numberOfConstraints):

	numberOfColumns = numberOfVariables #number of columns of the table disregarding the last column, which represents the vector b 

	#exhanging each free variable for two other non-negative variables
	#adding coefficients to the objective function 

	i = 0
	while i < len(nonNegativity):
		if nonNegativity[i] == 0:
			#matrix_constraints = np.insert(matrix_constraints, elem+1, matrix_constraints[:,elem], axis = 1)
			matrix_constraints = duplicate_column(matrix_constraints, i, 1)	
			matrix_constraints[:, i+1] = matrix_constraints[:, i+1]*(-1)  #column*(-1)
			nonNegativity = np.insert(nonNegativity, i+1, 1)
			objFunction = np.insert(objFunction, i+1, objFunction[i]*(-1))
			numberOfColumns += 1
		i += 1

	#changing all inequalities by equations by adding extra variables
	#adding 0's to the objective function in the end
	#adding the variables that can enter the base and saving the lines that are missing
	base = []
	missing_lines_id_matrix = []

	for i in range(0, len(symbols)):
		
		if(symbols[i] == '=='):
			missing_lines_id_matrix.append(i)

		elif symbols[i] == '<=':
			matrix_constraints = insert_identity_column(matrix_constraints, i, 1, numberOfColumns-1)
			objFunction = np.append(objFunction, 0)
			numberOfColumns += 1

			if(matrix_constraints[i][numberOfColumns] >= 0): 
				base_variable = []
				row_number = i #of the matrix_constraints
				column_number = numberOfColumns-1 #of the matrix_constraints
				base_variable.append(row_number)
				base_variable.append(column_number)
				base.append(base_variable)
			else: 
				missing_lines_id_matrix.append(i)

		elif symbols[i] == '>=':
			matrix_constraints = insert_identity_column(matrix_constraints, i, -1, numberOfColumns-1)
			objFunction = np.append(objFunction, 0)
			numberOfColumns += 1

			if(matrix_constraints[i][numberOfColumns] <= 0):
				base_variable = []
				row_number = i #of the matriz_constraints
				column_number = numberOfColumns-1 #of the matriz_constraints
				base_variable.append(row_number)
				base_variable.append(column_number)
				base.append(base_variable)

				matrix_constraints[i][:] *= -1
			else: 
				missing_lines_id_matrix.append(i)

	return matrix_constraints, objFunction, base, missing_lines_id_matrix

def exists_obvious_solution(base, numberOfConstraints):
	return len(base) == numberOfConstraints

def find_viable_solution(matrix_constraints, numberOfConstraints, objFunction, base, missing_lines_id_matrix):
	
	#inserting missing lines on the identity matrix (base)
	aux = 0
	for elem in missing_lines_id_matrix:

		column_index = len(objFunction)-1+aux #vector b's column index

		#making vector b > 0
		if(matrix_constraints[elem][column_index+1] < 0):
			matrix_constraints[elem][:] *= -1


		matrix_constraints = insert_identity_column(matrix_constraints, elem, 1, column_index)
		aux += 1
		
		#adding variables that were added to the base in the list 
		base_variable = []
		row_number = elem #of the matrix_constraints
		column_number = column_index+1 #of the matrix_constraints
		base_variable.append(row_number)
		base_variable.append(column_number)
		base.append(base_variable)
	
	numberOfVariablesOutOfBase = len(objFunction)+len(missing_lines_id_matrix)-numberOfConstraints
	func_aux = np.zeros(numberOfVariablesOutOfBase, dtype = Fraction)		#objective function of the auxiliary LP (PL auxiliar)
	ones = np.ones(numberOfConstraints, dtype = Fraction)
	func_aux = np.append(func_aux, ones)
	func_aux = np.append(func_aux, Fraction(0))	#this will be the value of the objective function

	tableau_aux = np.insert(matrix_constraints, 0, func_aux, axis = 0) #inserting aux PL's obj function to the matrix

	for i in range(0, len(base)):
		base[i][0] += 1

	tableau_aux = put_matrix_in_canonical_form(tableau_aux, base)

	tableau_aux, PLaux_status, base = simplex(tableau_aux, func_aux, numberOfConstraints, base)

	if(tableau_aux[0][len(func_aux)-1]) < 0:
		PLaux_status = "inviavel"

	return PLaux_status, tableau_aux, base

def put_matrix_in_canonical_form(tableau, base):
	
	for i in range(0, len(base)):
		tableau[0][:] += tableau[base[i][0]][:]*(-1) 
	
	return tableau

def gaussian_elimination(tableau, element_coordinate, numberOfConstraints):
	tableau[element_coordinate[0]][:] /= tableau[element_coordinate[0]][element_coordinate[1]]
	for row in range(0, numberOfConstraints+1):
		if row != element_coordinate[0]:
			opposite_number = (-1)*tableau[row][element_coordinate[1]]
			tableau[row][:] += opposite_number*tableau[element_coordinate[0]][:]
	return tableau

def simplex(tableau, objFunction, numberOfConstraints, base):
	PLstatus = "otimo"
	index_vector_b = len(objFunction)-1 #considering that the objective function already has its value appended at the end 
	possible = True

	while possible:

		for column in range(0, index_vector_b-1):
			possible = False
			if tableau[0][column] < 0:
				min_ratio = math.inf
				for row in range(1, numberOfConstraints+1):
					if(tableau[row][column] > 0): #!!!!estou considerando q o b sempre vai ficar + e portanto n vai influenciar a razao ser neg
						possible = True
						ratio = tableau[row][index_vector_b]/tableau[row][column]
						if ratio < min_ratio:
							min_ratio = ratio 
							min_ratio_coordinate = [row, column]
				
				if(min_ratio == math.inf):
					PLstatus = "ilimitado"
					break 
				else:
					tableau = gaussian_elimination(tableau, min_ratio_coordinate, numberOfConstraints)
					#updating base
					for i in range(0, len(base)):
						if(base[i][0] == min_ratio_coordinate[0]):
							index_base_variable = i;
							base[index_base_variable][1] = min_ratio_coordinate[1]
					break

	return tableau, PLstatus, base

def main():

	#open and reading the input file

	if len(sys.argv) != 3:
		print ("Usage: python simplex.py input.txt output.txt")
		sys.exit(1)

	with open(sys.argv[1]) as input_file:
		data = input_file.readlines()

	#extracting input data

	numberOfVariables = int(data[0])
	numberOfConstraints = int(data[1])
	nonNegativity =  [int(item) for item in data[2].split()]				#transforming each character of line 3 into an integer
	objFunction = np.array([Fraction(item) for item in data[3].split()])	#transforming each character of line 4 into a fraction

	matrix_constraints_list = []	#list of all constraints without the equality/inequality symbols
	symbols = []					#equality/inequality symbols

	for i in range(4, 4+numberOfConstraints):
		
		data_aux = data[i].split()

		constraint_line = []
		
		for j in range(0, numberOfVariables+2):

			if j != numberOfVariables:
				constraint_line.append(Fraction(data_aux[j]))
			else:
				symbols.append(data_aux[j])

		matrix_constraints_list.append(constraint_line)

	matrix_constraints = np.array(matrix_constraints_list)

	#creating initial tableau (FPI)
	matrix_constraints, objFunction, base, missing_lines_id_matrix = create_FPI_tableau(numberOfVariables, nonNegativity, symbols, matrix_constraints, objFunction, numberOfConstraints)

	if not exists_obvious_solution(base, numberOfConstraints):
		PLstatus, tableau_aux, base = find_viable_solution(matrix_constraints, numberOfConstraints, objFunction, base, missing_lines_id_matrix)
		if PLstatus == "inviavel":
			#open and writing the output_file
			with open(sys.argv[2], 'w') as output_file:
				print('Status: ', PLstatus, file = output_file)
				#print leaves a blank line - I didn't produce the certificates.
		else: 
			objFunction = np.append(objFunction, Fraction(0))	#this will be the value of the objective function
			objFunction *= -1
			tableau = np.delete(tableau_aux, 0, axis = 0) #deleting aux PL's obj function
			
			#deleting columns that were added
			column_indx = len(objFunction)+len(missing_lines_id_matrix)-2
			
			for i in range(0, len(missing_lines_id_matrix)):
				tableau = np.delete(tableau, column_indx-i, axis = 1)
			tableau = np.insert(tableau, 0, objFunction, axis = 0) #inserting PL's obj function to the matrix
			
			#making vector b > 0
			for row in range(1, numberOfConstraints+1):
				if(tableau[row][len(objFunction)-1] < 0):
					tableau[row][:] *= -1

			for elem in base:
				opposite_number = (-1)*tableau[0][elem[1]]
				tableau[0][:] += opposite_number*tableau[elem[0]][:]

			tableau, PLstatus, base = simplex(tableau, objFunction, numberOfConstraints, base)

	else: 
		objFunction = np.append(objFunction, Fraction(0))	#this will be the value of the objective function
		objFunction *= -1
		tableau = np.insert(matrix_constraints, 0, objFunction, axis = 0) #inserting PL's obj function to the matrix

		for row in range(1, numberOfConstraints+1):
			#making vector b > 0
			if(tableau[row][len(objFunction)-1] < 0):
				tableau[row][:] *= -1

		for i in range(0, len(base)):
			base[i][0] += 1

		tableau, PLstatus, base = simplex(tableau, objFunction, numberOfConstraints, base)

	#open and writing the output_file
	if(PLstatus == "ilimitado"):
		with open(sys.argv[2], 'w') as output_file:
			print('Status: ', PLstatus, file = output_file)
			#print leaves a blank line - I didn't produce the certificates.
	elif(PLstatus == "otimo"):
		with open(sys.argv[2], 'w') as output_file:
			numberVariables = len(objFunction)-1;
			print('Status: ', PLstatus, file = output_file)
			print('Objetivo: ', tableau[0][numberVariables], file = output_file)
			print('Solucao: ', file = output_file)
			base.sort(key = itemgetter(1))
			j = 0
			for i in range(0, numberVariables):
				if(j < len(base) and i == base[j][1]):
					output_file.write(str(tableau[base[j][0]][numberVariables]) + ' ')
					j += 1
				else:
					output_file.write('0 ')
			output_file.write('\n') #leaving a blank line because I didn't produce the certificates.

if __name__ == "__main__":
    main()