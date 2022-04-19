import { Schema, model as createModel, Document } from 'mongoose';
import Frame from '../interfaces/frame';
import MongoModel from './mongoModel';

interface FrameDocument extends Frame, Document { }

const frameSchema = new Schema<FrameDocument>({
  material: String,
  color: String,
});

class FrameModel extends MongoModel<Frame> {
  constructor(model = createModel('Armacoes', frameSchema)) {
    super(model);
  }
}

export default FrameModel;
