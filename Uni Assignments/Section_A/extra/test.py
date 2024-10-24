import matplotlib.pyplot as plt

# Data
acceleration = [0.028683094, 0, 0.039720744, 0, 0.055337857, 0, -0.081755559, -0.109911875, 0, 0]
m_over_M_plus_m = [0.024509804, 0.04784689, 0.070093458, 0.091324201, 0.111607143, 0.131004367, 0.14957265, 0.167364017, 0.18442623, 0.200803213]



plt.figure(figsize=(10, 6))
plt.plot(m_over_M_plus_m, acceleration, marker='o')
plt.title('test')
plt.xlabel('(m)/(M+m) (kg)')
plt.ylabel('Acceleration (m/s²)')
plt.axhline(0, color='red', lw=0.5, ls='--')  # Line at y=0 for reference
plt.grid()
plt.show()
