import { Schema, Document, Types } from 'mongoose';

export interface Tournament extends Document {
  year: number,
  hostCountry: string,
  runnerUp: string,
  editionGoals: number,
  editionStrikers: string[],
  bestPlayer?: string,
  bestGoalKeeper?: string,
  bestYoungPlayer?: string,
}

const cupSchema = new Schema<Tournament>({
  id: { type: Types.ObjectId },
  year: { type: Number, required: true },
  hostCountry: { type: String, required: true },
  runnerUp: { type: String, required: true },
  editionGoals: { type: Number, required: true },
  editionStrikers: { type: [String], required: true },
  bestPlayer: { type: String, required: false },
  bestGoalKeeper: { type: String, required: false },
  bestYoungPlayer: { type: String, required: false },
})

export default cupSchema;
