import numpy as np
import matplotlib.pyplot as plt


def cosine_beta(t, s):
    output = np.cos((t + s) / (1 + s) * np.pi / 2) ** 2
    return output / output[0]

# 테스트를 위한 timesteps과 s 파라미터 설정
timesteps = np.linspace(0, 1, 100)  # 0부터 1까지 100개의 timestep
s = 0.008  # s 파라미터

# cosine-beta 함수 적용
cosine_beta_values = cosine_beta(timesteps, s)

# 결과 시각화
plt.plot(timesteps, cosine_beta_values)
plt.title('Cosine Beta Function')
plt.xlabel('Timesteps')
plt.ylabel('Value')
plt.show()

#
# def cosine_beta(t, s):
#     output = np.cos((t + s) / (1 + s) * np.pi / 2) ** 2
#     return output / output[0]
#
#
# # Define the function gamma(t)
# def cosine(t, s, e, tau):
#     v_start = np.cos(np.pi * s / 2) ** (2 * tau)
#     v_end = np.cos(np.pi * e / 2) ** (2 * tau)
#     temp = np.cos(np.pi * ((t * (e - s) + s) / 2)) ** (2 * tau)
#     return (v_end - temp) / (v_end - v_start)
#
#
# def sigmoid(t, s, e, tau):
#     def sig(x):
#         return 1 / (1 + np.exp(-x))
#
#     ve = sig(e / tau)
#     vs = sig(s / tau)
#     temp = sig((t * (e - s) + s) / tau)
#
#     return (ve - temp) / (ve - vs)
#
#
# # Parameters
# sig_title = 'Sigmoid-based'
# cos_title = 'Cosine-based'
# # s = 0    # Start time
# # e = -3    # End time
# # tau = 0.9  # This can be adjusted
# title = sig_title
#
# # Generate a range of t values
# t = np.linspace(0, 1, 1000)
#
# # Plot the function
# plt.figure(figsize=(7, 5))
#
# # # Calculate gamma(t) values
# # y1 = [sigmoid(t, 0, 3, 0.3) for t in t]
# # y2 = [sigmoid(t, 0, 3, 0.7) for t in t]
# # y4 = [sigmoid(t, -3, 3, 0.9) for t in t]
# # y5 = [sigmoid(t, -3, 3, 10) for t in t]
# # y6 = [sigmoid(t, -3, 3, 0.5) for t in t]
# # y7 = [sigmoid(t, -3, 3, 0.3) for t in t]
# #
# # plt.plot(t, y7, label=r'$s = -3, e = 3, \tau = 0.3$')
# # plt.plot(t, y6, label=r'$s = -3, e = 3, \tau = 0.5$')
# # plt.plot(t, y4, label=r'$s = -3, e = 3, \tau = 0.9$')
# # plt.plot(t, y5, label=r'$s = -3, e = 3, \tau = 10$')
# # plt.plot(t, y2, label=r'$s = 0, e = 3, \tau = 0.7$')
# # plt.plot(t, y1, label=r'$s = 0, e = 3, \tau = 0.3$')
# # plt.title(sig_title)
#
# y_origin = [cosine_beta(t, 0.008) for t in t]
# y22 = [sigmoid(t, -3, 3, 0.3) for t in t]
# y1 = [cosine(t, 0.2, 1, 5) for t in t]
# y2 = [cosine(t, 0.2, 1, 3) for t in t]
# y4 = [cosine(t, 0.2, 1, 2) for t in t]
# y5 = [cosine(t, 0.2, 1, 1) for t in t]
# y6 = [cosine(t, 0, 1, 1) for t in t]
# y7 = [cosine(t, 0, 0.2, 1) for t in t]
# y8 = [cosine(t, 0, 0.8, 1) for t in t]
# plt.plot(t, y_origin, label=r'$cos_beta, s = 0.008$')
# plt.plot(t, y22, label=r'$sigmoid, s = -3, e = 3, \tau = 0.3$')
# plt.plot(t, y7, label=r'$s = 0, e = 0.2, \tau = 1$')
# plt.plot(t, y8, label=r'$s = 0, e = 0.8, \tau = 1$')
# plt.plot(t, y6, label=r'$s = 0, e = 1, \tau = 1$')
# plt.plot(t, y5, label=r'$s = 0.2, e = 1, \tau = 1$')
# plt.plot(t, y4, label=r'$s = 0.2, e = 1, \tau = 2$')
# plt.plot(t, y2, label=r'$s = 0.2, e = 1, \tau = 3$')
# plt.plot(t, y1, label=r'$s = 0.2, e = 1, \tau = 5$')
# plt.title(cos_title)
#
# plt.xlabel('t')
# plt.ylabel(r'$\gamma(t)$')
# plt.grid(False)
# plt.legend()
# plt.show()
