import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 200)

# 1. 원
x = np.cos(t)*2
y = np.sin(t)*2

# 2~3. 그리기
plt.plot(x, y)
x8=np.sin(t)
y8=np.sin(t)*np.cos(t)
plt.plot(x8, y8)

# 4. 검증
points=np.stack([x,y],axis=1)
print(points.shape)
dist=np.linalg.norm(points,axis=1)
print(np.allclose(dist,2))

plt.axis('equal')
plt.title('Unit Circle')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
