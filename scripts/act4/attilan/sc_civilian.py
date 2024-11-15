# Generated by BehavEd
# ( "comment" )
rand_pos = randomInt(1, 1 )
if rand_pos == 1
     # ( "Person sits in chair" )
     rand_chair = randomInt(1, 6 )
     check_chair = getZoneFlag("chair", rand_chair )
     if check_chair == 1
          check_stand = getZoneFlag("stand", rand_chair )
          time = randomInt(1, 3 )
          if check_stand == 1
               rand_path = randomInt(1, 6 )
               rand_pos = randomInt(8, 12 )
               if rand_path == 1
                    waittimed ( time )
                    setWaypointPath("_OWNER_", "outer_circle", rand_pos )
               elif rand_path < 4
                    waittimed ( time )
                    setWaypointPath("_OWNER_", "inner_circle", rand_pos )
               else
                    waittimed ( time )
                    setWaypointPath("_OWNER_", "royal_circle", rand_pos )
               endif
          else
               setZoneFlag("stand", rand_chair, 1 )
               # ( "**************This forces the character into a spot next to a chair**************" )
               stand_name = strcatint("peeping", rand_chair )
               copyOriginAndAngles("_OWNER_", stand_name )
               rand_civtalk = randomInt(1, 3 )
               if rand_civtalk == 1
                    playanim (  "EA_TALKING_01", "_OWNER_", "LOOP", "" )
               elif rand_civtalk == 2
                    playanim (  "EA_TALKING_02", "_OWNER_", "LOOP", "" )
               elif rand_civtalk == 3
                    playanim (  "EA_TALKING_03", "_OWNER_", "LOOP", "" )
               endif
          endif
     else
          setZoneFlag("chair", rand_chair, 1 )
          # ( "**************This forces the character into a chair**************" )
          chair_name = strcatint("seat", rand_chair )
          copyOriginAndAngles("_OWNER_", chair_name )
          playanim (  "EA_ZONE8", "_OWNER_", "LOOP", "" )
     endif
endif

