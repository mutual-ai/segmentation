import numpy as np
import keras.preprocessing.image

def data_from_array(data_dir):
    # load  x
    training_x = np.load(data_dir+"training/x.npy")
    test_x = np.load(data_dir+"test/x.npy")
    validation_x = np.load(data_dir+"validation/x.npy")

    print(training_x.shape)
    print(test_x.shape)
    print(validation_x.shape)

    # normalize
    training_x = training_x / 255
    test_x = test_x / 255
    validation_x = validation_x / 255

    # load y
    training_y = np.load(data_dir+"training/y.npy")
    test_y = np.load(data_dir+"test/y.npy")
    validation_y = np.load(data_dir+"validation/y.npy")

    print(training_y.shape)
    print(test_y.shape)
    print(validation_y.shape)
    
    return [training_x, training_y, validation_x, validation_y, test_x, test_y]

def data_from_images(data_dir, batch_size, bit_depth, dim1, dim2):
    
    flow_train = single_data_from_images(data_dir + 'training/', batch_size, bit_depth, dim1, dim2)
    flow_validation = single_data_from_images(data_dir + 'validation/', batch_size, bit_depth, dim1, dim2)
    flow_test = single_data_from_images(data_dir + 'test/', batch_size, bit_depth, dim1, dim2)
    
    return [flow_train, flow_validation, flow_test]

def single_data_from_images(data_dir, batch_size, bit_depth, dim1, dim2):

    rescale_factor = 1./(2**bit_depth - 1)

    gen_x = keras.preprocessing.image.ImageDataGenerator(rescale=rescale_factor)
    gen_y = keras.preprocessing.image.ImageDataGenerator()
    
    seed = 42

    stream_x = gen_x.flow_from_directory(data_dir + 'x/',
                                                           target_size=(dim1,dim2),
                                                           color_mode='grayscale',
                                                           batch_size=batch_size,
                                                           class_mode=None,
                                                           seed=seed)
    stream_y = gen_y.flow_from_directory(data_dir + 'y/',
                                                           target_size=(dim1,dim2),
                                                           color_mode='rgb',
                                                           batch_size=batch_size,
                                                           class_mode=None,
                                                           seed=seed)
    
    flow = zip(stream_x, stream_y)
    
    return flow
