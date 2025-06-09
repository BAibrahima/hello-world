class Livre:
	def __init__(self,titre,auteur,annee_publication):
		self.titre=titre
		self.auteur=auteur
		self.annee_publication=annee_publication
		self.disponible=True

	def emprunter(self):
		if self.disponible:
			self.disponible =False
			print(f"le livre: {self.titre} a été emprunter")

		else :
			print(f"le livre: {self.titre} n'est pas disponible")

	def retourner(self):
		if not self.disponible:
			self.disponible = True
			print(f"le livre: {self.auteur} a été retourné")

		else :
			print(f"le livre: {self.titre} n'a pas été emprunté")
 
	def afficher_info(self):

		statut="disponible" if self.disponible else "emprunté"
		print(f"le livre: {self.titre} dont l'auteur est {self.auteur} publié en {self.annee_publication} est {statut}")


