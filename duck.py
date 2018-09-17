class Duck:
    
	sound = 'fart'
	walking = 'wonky walk'
	
	def quack(self):
		print(self.sound)
		print('Aflac')
	def walk(self):
		print('Bitch walks like a duck')
		print(self.walking)
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
if __name__ == '__main__': main()
