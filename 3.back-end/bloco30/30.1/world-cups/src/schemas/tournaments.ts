import { Schema } from 'mongoose';

export interface Tournament {
  year: number,
  hostCountry: string,
  runnerUp: string,
  editionGoals: number,
  editionStrikers: string[],
  bestPlayer: string,
  bestGoalKeeper: string,
  bestYoungPlayer: string,
}

const cupSchema = new Schema<Tournament>({
  year: { type: Number, required: true },
  hostCountry: { type: String, required: true },
  runnerUp: { type: String, required: true },
  editionGoals: { type: Number, required: true },
  editionStrikers: { type: [String], required: true },
  bestPlayer: { type: String, required: true },
  bestGoalKeeper: { type: String, required: true },
  bestYoungPlayer: { type: String, required: true },
})

export default cupSchema;
