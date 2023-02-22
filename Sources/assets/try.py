import random


class Chest:
    def __init__(self) -> None:
        chest_1 = [
            "Barbell bench press 4 sets of 8-12 reps",
            "Incline dumbbell press 3 sets of 8-12 reps",
            "Dumbbell flyes 3 sets of 12-15 reps",
            "Cable crossovers 3 sets of 12-15 reps",
            "Dips 3 sets of 8-12 reps"
        ]

        chest_2 = [
            "Dumbbell bench press 4 sets of 8-12 reps",
            "Incline barbell press 3 sets of 8-12 reps",
            "Cable flyes 3 sets of 12-15 reps",
            "Push-ups 4 sets of 8-12 reps",
            "Pull-ups 3 sets of 8-12 reps"
        ]

        chest_3 = [
            "Barbell incline press 4 sets of 8-12 reps",
            "Decline dumbbell press 3 sets of 8-12 reps",
            "Inverted rows 3 sets of 12-15 reps",
            "Dumbbell pullovers 3 sets of 12-15 reps",
            "Ring push-ups 3 sets of 8-12 reps"
        ]

        chest_4 = [
            "Dumbbell incline press 4 sets of 8-12 reps",
            "Decline barbell press 3 sets of 8-12 reps",
            "Chest press machine 3 sets of 12-15 reps",
            "Pec deck fly 3 sets of 12-15 reps",
            "Smith machine press 3 sets of 8-12 reps"
        ]

        chest_5 = [
            "Barbell decline press 4 sets of 8-12 reps",
            "Flat dumbbell press 3 sets of 8-12 reps",
            "Chest fly machine 3 sets of 12-15 reps",
            "Cable pullovers 3 sets of 12-15 reps",
            "Medicine ball push-ups 3 sets of 8-12 reps"
        ]

        chest_6 = [
            "Incline dumbbell press 4 sets of 8-12 reps",
            "Flat barbell press 3 sets of 8-12 reps",
            "Dumbbell pullovers 3 sets of 12-15 reps",
            "Cable crossovers 3 sets of 12-15 reps",
            "Bodyweight dips 3 sets of 8-12 reps"
        ]

        chest_7 = [
            "Decline dumbbell press 4 sets of 8-12 reps",
            "Incline barbell press 3 sets of 8-12 reps",
            "Chest press machine 3 sets of 12-15 reps",
            "Pec deck fly 3 sets of 12-15 reps",
            "Smith machine press 3 sets of 8-12 reps"
        ]

        chest_8 = [
            "Flat dumbbell press 4 sets of 8-12 reps",
            "Barbell decline press 3 sets of 8-12 reps",
            "Chest fly machine 3 sets of 12-15 reps",
            "Cable pullovers 3 sets of 12-15 reps",
            "Medicine ball push-ups 3 sets of 8-12 reps"

        ]

        chest_9 = [
            "Flat barbell press 4 sets of 8-12 reps",
            "Incline dumbbell press 3 sets of 8-12 reps",
            "Dumbbell pullovers 3 sets of 12-15 reps",
            "Cable crossovers 3 sets of 12-15 reps",
            "Bodyweight dips 3 sets of 8-12 reps"
        ]

        chest_10 = [
            "Barbell bench press 4 sets of 8-12 reps",
            "Dumbbell bench press 3 sets of 8-12 reps",
            "Incline bench press 3 sets of 12-15 reps",
            "Decline bench press 3 sets of 12-15 reps",
            "Dumbbell flyes 3 sets of 8-12"
        ]

        self.chest_focused = {
            1: chest_1,
            2: chest_2,
            3: chest_3,
            4: chest_4,
            5: chest_5,
            6: chest_6,
            7: chest_7,
            8: chest_8,
            9: chest_9,
            10: chest_10
        }

    def get_a_workout(self):
        ran = random.randint(1, 11)
        return (self.chest_focused[ran])


Workout = Chest()
print(Workout.get_a_workout())