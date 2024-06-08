mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
missionNamesAndYears = zip(mission_names, mission_years)
success = 0
totalMissions = 0

# wow, I had absolutely no idea that first part of the for loop was just an arbitrary variable you can set. It can be "i" "success_status" or literally anything else.
# So basically I can use that as additional context for someone else who is going to be reading my code. While it could be an arbitrary variable, I can use it instead
# as something to basically help people understand what I'm doing / trying to do.

for total in mission_success:
    totalMissions += 1

for success_status in mission_success:
    if success_status == True:
        success += 1

successRate = success / totalMissions * 100

print(f"Total number of missions: {totalMissions}")
print(f"Total number of successful missions: {success}")
print(f"Sucess rate: {successRate:.2f}%")
print("Missions launched before the year 2000:")
for name, year in missionNamesAndYears:
    if year < 2000:
        print(f"{name}")
