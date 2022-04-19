import { Schema, model as createModel, Document } from 'mongoose';
import Lens from '../interfaces/lens';
import MongoModel from './mongoModel';

interface LensDocument extends Lens, Document { }

const lensSchema = new Schema<LensDocument>({
  degree: Number,
  antiGlare: Boolean,
  blueLightFilter: Boolean,
});

class LensModel extends MongoModel<Lens> {
  constructor(model = createModel('Lenses', lensSchema)) {
    super(model);
  }
}

export default LensModel;
