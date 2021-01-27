# Importing the necessary modules
import dendropy

# Specifying the paths of our tree list(s). Include full path if not in wd
file1 = "ERLEC_NT.trees"
#file2 = "ERLEC_AA.trees"

# Reads our tree list(s) into a dendropy dataset under a common taxon namespace
# Edit to add a second tree list
namespace = dendropy.TaxonNamespace()
trees = dendropy.DataSet()
trees.attach_taxon_namespace(namespace)
tree_list1 = trees.new_tree_list()
tree_list1.read(path=file1, schema='newick')
#tree_list2 = trees.new_tree_list()
#tree_list2.read(path=file2, schema='newick')

# Function that accepts one list of trees, iterating over each tree to calculate the distance between it and
# every other tree (excluding itself)
# uses indexing magic to avoid redundant calculations
def one_list(list1):
	with open('distances.csv', 'wb') as f:
		for i in range(len(list1)-1):
			ls = range(i+1, len(list1))
			for j in ls:
				f.write(str(dendropy.calculate.treecompare.symmetric_difference(list1[i], list1[j])))
				f.write('\n')
			print 'Tree ' + str(i+1)

# Function that accepts two lists of trees, iterating over each tree in the first list and calculating the distance
# between it and every tree in the second list
def two_list(list1, list2):
	with open('distances.csv', 'wb') as f:
		for i in range(len(list1)):
			for j in range(len(list2)):
				f.write(str(dendropy.calculate.treecompare.symmetric_difference(list1[i], list2[j])))
				f.write('\n')
			print 'Tree ' + str(i+1)

one_list(tree_list1)
#two_list(tree_list1, tree_list2)
