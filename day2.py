import numpy as np

def rot(theta):
    """2x2 회전 행렬"""
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]])

def T(x, y, theta):
    """3x3 동차 변환 행렬"""
    return np.array([[np.cos(theta), -np.sin(theta), x],
                     [np.sin(theta),  np.cos(theta), y],
                     [0, 0, 1]])

def apply(Tm, p):
    """점 p=(px, py)를 변환해서 (2,) 배열로 돌려주기"""
    p_homogeneous = np.array([p[0], p[1], 1])  # 점을 동차 좌표로 변환
    transformed_p = Tm @ p_homogeneous  # 행렬 곱 수행
    return transformed_p[:2]  # 결과를 (2,) 배열로 반환


def inv(Tm):
    """역변환 (np.linalg.inv 쓰지 말고 직접!)"""
    R = Tm[:2, :2]  # 회전 부분
    t = Tm[:2, 2]   # 평행 이동 부분

    R_inv = R.T  # 회전 행렬의 역행렬은 전치 행렬
    t_inv = -R_inv @ t  # 평행 이동의 역변환

    Tm_inv = np.eye(3)  # 3x3 단위 행렬 생성
    Tm_inv[:2, :2] = R_inv
    Tm_inv[:2, 2] = t_inv

    return Tm_inv

if __name__ == "__main__":
    d = np.deg2rad
    print("test1:", np.allclose(apply(T(2, 1, d(90)), (1, 0)), [2, 2]))
    print("test2:", np.allclose(apply(T(2, 1, d(90)), (0, 1)), [1, 1]))
    print("test3:", np.allclose(apply(T(0, 0, d(0)), (1, 0)), [1, 0]))
    print("test4:", np.allclose(apply(T(0, 0, d(0)), (0, 1)), [0, 1]))
    print("test5:", np.allclose(apply(T(0, 0, d(90)), (1, 0)), [0, 1]))
    
    print("test6:", np.allclose(apply(inv(T(2, 1, d(90))), (2, 2)), [1, 0]))
    print("test7:", np.allclose(T(2, 1, 0.7) @ inv(T(2, 1, 0.7)), np.eye(3)))
    print("test8:", np.allclose(inv(T(2, 1, 0.7)) @ T(2, 1, 0.7), np.eye(3)))