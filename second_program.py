from multiprocessing import Process
import first_program

arrays = ([1, 2, 3, 4, 5], [12, 4, 1, 5, 8, 10], [11, 23, 1, 7, 3, 4, 1, 9, 10])

if __name__ == '__main__':
    processes = []
    for s_arr in arrays:
        MeanProcess = Process(target=first_program.mean_of_array, args=[s_arr])
        VarProcess = Process(target=first_program.var_of_array, args=[s_arr])

        MeanProcess.start()
        VarProcess.start()

        processes.append(MeanProcess)
        processes.append(VarProcess)

    [process.join() for process in processes]

    print('NICE')
