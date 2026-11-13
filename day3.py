import numpy as np
import matplotlib.pyplot as plt

R, L, dt = 0.05, 0.24, 0.01

def step(state, wl, wr):
    x, y, th = state
    v = R*(wl + wr)/2  # TODO: 전진은 평균
    w = R*(wr-wl)/L  # TODO: 회전은 차이
    
    # TODO: x, y, th를 dt만큼 업데이트
    x += v * np.cos(th) * dt
    y += v * np.sin(th) * dt
    th += w * dt
    return np.array([x, y, th])

def simulate(wl, wr, T_end=None):
    w = R * (wr - wl) / L
    if w == 0:
        T_lap = np.inf          # 영원히 한 바퀴를 못 돎 → 바퀴를 안 바꿈
        if T_end is None:
            T_end = 10.0        # 직진은 그냥 10초
    else:
        T_lap = 2 * np.pi / abs(w)
        if T_end is None:
            T_end = 2 * T_lap
    state = np.array([0.0, 0.0, 0.0])
    traj = [state]
    for k in range(int(T_end / dt)):
        t=k*dt
        if t<T_lap:
            state = step(state, wl, wr)
            traj.append(state)
        else:
            state = step(state, wr, wl)
            traj.append(state)
    return np.array(traj)
if __name__ == "__main__":
    traj = simulate(wl=10.0, wr=10.0)
    plt.plot(traj[:, 0], traj[:, 1])
    plt.axis("equal")
    plt.grid()
    plt.show()

