w = 1000 #backround size
h = 800
p_infection = 0.05 #infected probability
n_people = 200


class Person():
    def __init__(self,id, x,y,vx,vy):
        self.id = id
        self.x = x #location
        self.y = y 
        self.vx = vx # direction
        self.vy = vy
        self.status = 'normal' #infected
        
    def move(self):
        if self.x < 0 or self.x > w:
            self.vx *= -1 #if crash side, change direction
        if self.y < 0 or self.y > h:
            self.vy *= -1 
        
        self.x += self.vx
        self.y += self.vy
   
    def display(self):
        if self.status =='infected':
            fill(255,0,0)
        elif self.status =='gohome_infected':
            fill(0,0,255)
            self.vx = 0
            self.vy = 0
        elif self.status == 'gohome_normal':
            fill(0,255,0)
            self.vx = 0
            self.vy = 0
        else:
            fill(127)
                
        ellipse(self.x, self.y, 10 ,10)
    
    def collide(self): #centers distance < circle's 2r
        for i in range(self.id+1, len(people)):
            person = people[i]
            
            if self.status in ['gohome_normal' , 'gohome_infected'] or person.status in ['gohome_normal' , 'gohome_infected']:
                continue
            
            distance = sqrt((self.x - person.x)**2 +(self.y-person.y)**2)
            
            if distance < 20:
                p_people = random(0,1)
                if self.status == 'infected' and person.status == 'normal' and p_people < p_infection:
                    person.status = 'infected'
                elif self.status == 'normal' and person.status == 'infected' and p_people < p_infection:
                    self.status = 'infected'
    
    def gohome(self):
        if self.status == 'normal' and self.x >= 950 and self.y >= 760:
            self.status = 'gohome_normal'

        elif self.status == 'infected' and self.x >= 950 and self.y >= 760:
            self.status = 'gohome_infected'
  """          
    def people_infect_pro():
        p_people = random(0,1)
        data = {0.0: 0.8855538342370256, 0.14: 0.9539116963594113, 0.28: 0.9752130131680867, 
                0.42: 0.9870255615801704, 0.57: 0.9922540666150271, 0.71: 0.9936096049573974, 
                0.85: 0.9949651432997676, 1.0: 0.9957397366382649, 1.14: 0.9965143299767621, 
                1.28: 0.9967079783113865, 1.42: 0.9970952749806351, 1.57: 0.9976762199845081, 
                1.71: 0.9978698683191324, 2.14: 0.998257164988381, 2.42: 0.9986444616576297, 
                2.57: 0.998838109992254, 3.0: 0.9992254066615026, 3.42: 0.9996127033307513, 3.85: 0.9998063516653756, 7.28: 0.9999999999999999}
        for i in range(len(data)):
            if p_people < data[i]:
                p_people = random(0,1)
                if p_people
            
     """   
                
people = []
people_infected = []
people_infected_gohome = []

for i in range(n_people):
    person = Person(i,random(w), random(h), random(0, 5), random(0, 5))
    people.append(person)

people[0].status = 'infected' #you can change infected person    
    
def setup():
    global w, h
    size(w,h)
    background(32)
    
def draw():
    background(32)
    
    board = {
        'normal': 0,
        'infected': 0,
        'gohome_normal' :0,
        'gohome_infected' :0
        }
    
    for person in people:
        person.move()
        person.collide()
        person.gohome()
        person.display()
        
        board[person.status]+=1
    
    for i, (status,n) in enumerate(board.items()):
        textSize(16)
        fill(127)
        text("%s: %d" % (status,n) ,5 ,20 * (i+1))
    
