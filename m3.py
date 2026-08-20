import matplotlib.pyplot as plt
import pandas as pd

student1={'Monthly':['feb','apr','june','sep','nov','dec'],
          'Eng':[45,67,78,58,87,89],
          'Maths':[55,87,98,88,97,69]
          }
df=pd.DataFrame(student1)
df['Total']=df['Eng']+df['Maths']
df['PCT']=df['Total']/2

plt.scatter('Monthly','PCT',s=50,color='r',data=df)
plt.xlabel('Monthly Exam')
plt.ylabel('Percentage')
plt.title('Compare percentage of Two student')
plt.show()