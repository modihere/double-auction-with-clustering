import math
import random
import plotly
from plotly.graph_objs import Scatter, Scatter3d, Layout
#except ImportError:
   
 #print "INFO: Plotly is not installed, plots will not be generated."
num_clusters=7
def main():

    # How many points are in our dataset?
    num_points = 100

    # For each of those points how many dimensions do they have?
    dimensions = 2

    # Bounds for the values of those points in each dimension
    lower = 0
    upper = 200

    # The K in k-means. How many clusters do we assume exist?

    # When do we say the optimization has 'converged' and stop updating clusters
    cutoff = 0.2

    # Generate some points to cluster and their bid price arrival time and departure time as well in pointer.txt
    points = [makeRandomPoint(dimensions, lower, upper,i) for i in range (num_points)]
    print(points)
    #prices=[random.randint(1,num_points) for i in range(num_points)]
    #arrival_time=[random.randint(1,21) for i in range(num_points)]
    #departure_time=[arrival_time[i]+random.randint(1,3) for i in range(num_points)]
    pointfile=open("pointer.txt","w")
    new_pointfile=open("pointer_new.txt","w")
    
    #generate the buyer list in another text file with their budget.
    prices=[random.randint(30,45) for i in range(10)]
    f=open("buyer.txt","w")
    for i in range (10):
        f.write(str(prices[i])+" "+str(i)+"\n")


    # Cluster those data!
    clusters = kmeans(points, num_clusters, cutoff)
    #identify the agents
    agent_no=0
    # Print our clusters
    for i, c in enumerate(clusters):
        for p in c.points:
            print (" Cluster: ", i, "\t Point :", p)
            prices=random.randint(10,num_points)
            arrival_time=random.randint(10,15)
            departure_time=arrival_time+random.randint(1,3)
            agent_no+=1
            pointfile.write(str(p)+" "+str(i)+" "+str(prices)+" "+str(arrival_time)+" "+str(departure_time)+" "+str(agent_no)+"\n")
            new_pointfile.write(str(p)+" "+str(prices)+" "+str(arrival_time)+" "+str(departure_time)+" "+str(agent_no)+"\n")
    new_pointfile.close()
    # Display clusters using plotly for 2d data
    #print("data written in file for more usage. Do you want to see the plot of the data?\n")
    '''if dimensions in [2, 3] and plotly:
        print ("Plotting points, launching browser ...")
        plotClusters(clusters, dimensions)
    else:
        return
        '''

class Point(object):
    '''
    A point in n dimensional space
    '''
    def __init__(self, coords):
        '''
        coords - A list of values, one per dimension
        '''

        self.coords = coords
        self.n = len(coords)

    def __repr__(self):
        return str(self.coords)

class Cluster(object):
    '''
    A set of points and their centroid
    '''

    def __init__(self, points):
        '''
        points - A list of point objects
        '''

        if len(points) == 0:
            raise Exception("ERROR: empty cluster")

        # The points that belong to this cluster
        self.points = points

        # The dimensionality of the points in this cluster
        self.n = points[0].n

        # Assert that all points are of the same dimensionality
        for p in points:
            if p.n != self.n:
                raise Exception("ERROR: inconsistent dimensions")

        # Set up the initial centroid (this is usually based off one point)
        self.centroid = self.calculateCentroid()

    def __repr__(self):
        '''
        String representation of this object
        '''
        return str(self.points)

    def update(self, points):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        Note: Initially we expect centroids to shift around a lot and then
        gradually settle down.
        '''
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid)
        return shift

    def calculateCentroid(self):
        '''
        Finds a virtual center point for a group of n-dimensional points
        '''
        numPoints = len(self.points)
        # Get a list of all coordinates in this cluster
        coords = [p.coords for p in self.points]
        # Reformat that so all x's are together, all y'z etc.
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]

        return Point(centroid_coords)

def kmeans(points, k, cutoff):

    # Pick out k random points to use as our initial centroids
    initial = random.sample(points, k)              

    # Create k clusters using those centroids
    # Note: Cluster takes lists, so we wrap each point in a list here.
    clusters = [Cluster([p]) for p in initial]

    # Loop through the dataset until the clusters stabilize
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [[] for _ in clusters]
        clusterCount = len(clusters)

        # Start counting loops
        loopCounter += 1
        # For every point in the dataset ...
        for p in points:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(p, clusters[0].centroid)

            # Set the cluster this point belongs to
            clusterIndex = 0

            # For the remainder of the clusters ...
            for i in range(clusterCount - 1):
                # calculate the distance of that point to each other cluster's
                # centroid.
                distance = getDistance(p, clusters[i+1].centroid)
                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i+1
            # After finding the cluster the smallest distance away
            # set the point to belong to that cluster
            lists[clusterIndex].append(p)

        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0

        # For each cluster ...
        for i in range(clusterCount):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])
            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)

        # If the centroids have stopped moving much, say we're done!
        if biggest_shift < cutoff:
            print ("Converged after %s iterations" % loopCounter)
            break
    return clusters

def getDistance(a, b):
    '''
    Euclidean distance between two n-dimensional points.
    https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions
    Note: This can be very slow and does not scale well
    '''
    if a.n != b.n:
        raise Exception("ERROR: non comparable points")

    accumulatedDifference = 0.0
    for i in range(a.n):
        squareDifference = pow((a.coords[i]-b.coords[i]), 2)
        accumulatedDifference += squareDifference
    distance = math.sqrt(accumulatedDifference)

    return distance

def makeRandomPoint(n, lower, upper,val):
    '''
    Returns a Point object with n dimensions and values between lower and
    upper in each of those dimensions
    '''
    p1=[[126.02785491551988, 21.896185927707634], [27.154549647501568, 102.00380859352956], [28.68484982258439, 64.933636400464], [150.84514775902906, 192.7196010116338], [85.8976575181061, 132.91372804117395], [31.81830718488632, 124.86392070607766], [161.84979616146572, 68.37165103214535], [104.95585432574765, 76.14858465522335], [72.532760886891, 99.23934223537216], [137.35220155117167, 21.472211212798918], [18.3302756147951, 86.18017118086176], [48.274138360746186, 92.8273120550607], [15.760344041254303, 26.734182904524072], [108.04272527157912, 194.02663401726767], [61.331369520205904, 155.69880167134718], [78.28123901855028, 156.7605953835386], [198.04745402388951, 187.41737156685844], [75.49088086913251, 62.26196774523898], [181.45628605037166, 159.96351756956534], [150.61758463209733, 169.70715268752886], [89.30031884005436, 186.83330973317308], [64.0890230164089, 154.84530185061527], [152.56785377847808, 1.9218157492057575], [74.72783328908174, 160.3632059540249], [63.39570938856745, 143.13535206876213], [170.80909147863622, 148.75319447031237], [135.3786444087534, 42.943300968541195], [17.081337575392585, 66.02063420918634], [155.86058629695614, 146.51748002545702], [104.93379587483005, 77.29518101329293], [170.67139911244652, 104.55715787701865], [12.873380391647803, 167.7468447406055], [60.94451106731189, 47.78940437031309], [189.46942553614969, 11.14533676158791], [187.97886059152984, 143.5622689200337], [29.97874454920515, 183.1869254704966], [185.46407066624806, 48.9419147240747], [112.18970171624676, 74.4451161104437], [3.8247501865145583, 157.79772357308568], [128.12408537437065, 103.39171921188593], [54.067761709592354, 34.550956423450096], [150.2085048205141, 162.58046980277027], [27.885488577844075, 82.42228967416092], [97.90966379952644, 129.65810257218394], [112.04976626165424, 11.347497782179271], [109.29854098714257, 83.56437164707411], [29.194308762851428, 13.203076470917452], [114.44787683902011, 103.81796113419742], [23.12906454750332, 134.21522515628718], [195.3091143726577, 180.2574412704058], [63.28716660623827, 162.12869107156237], [112.7425538255631, 125.61994501496142], [60.23427260316774, 158.33692286946948], [182.31430222986847, 160.91165567212698], [158.71030644263905, 86.22542819694074], [187.97522870279235, 175.34017539765517], [65.68208395712492, 153.06872918987142], [60.433607300991234, 116.43945077301987], [89.81826894081655, 57.40163141808685], [10.16339184136228, 154.40531397875355], [126.3328672786053, 71.77896046493548], [42.211852496513046, 6.4441148004328985], [170.21554279958102, 4.718248671462799], [55.53513099514922, 115.19413765852484], [63.409946889298084, 158.92870015168876], [38.46941515246915, 67.82941829016384], [102.69006044898548, 4.440295851350173], [55.17117784010161, 67.16026686788246], [152.050455447002, 86.74858985220853], [75.80182537193738, 102.45567491822543], [165.02825060033504, 106.76039617290778], [17.659896385301277, 166.82341059052922], [141.12824343260348, 58.89584005005047], [43.398524045098384, 35.413572865852274], [82.38871722371945, 167.8663825249771], [98.28145625726808, 91.36476965176121], [130.56876242853957, 43.62961926090028], [60.40665894902666, 40.744650520985836], [119.26643047728842, 120.32272549885658], [133.7968380281946, 73.02325146846067], [102.3462194488977, 147.4835886828767], [87.75374334751336, 197.41489141155853], [130.32258654387465, 190.70254801041642], [24.319534837033217, 92.12019906761326], [109.882157429952, 96.2105704465642], [18.846868288019223, 104.03209636572446], [185.0362872085634, 139.14648470877356], [19.160911419164073, 100.53083060685577], [157.39932071270664, 2.887121926830205], [87.34759571217442, 37.29435083942108], [78.75580538905722, 111.92052507816896], [82.89988578721706, 186.65520276990566], [21.228435440862526, 151.61633583006403], [169.16302232546388, 49.79041320675035], [125.38161962159941, 195.58782879927995], [128.1868023182746, 193.24548735548348], [95.77565362818959, 192.27260452144503], [93.5606105180458, 181.28904728845814], [196.7448074753934, 127.54496218874718], [46.364642341681495, 154.64069125900522]]
    p = Point(p1[val])
    return p

def plotClusters(data, dimensions):
    '''
    This uses the plotly offline mode to create a local HTML file.
    This should open your default web browser.
    '''
    if dimensions not in [2, 3]:
        raise Exception("Plots are only available for 2 and 3 dimensional data")

    # Convert data into plotly format.
    traceList = []
    for i, c in enumerate(data):
        # Get a list of x,y coordinates for the points in this cluster.
        cluster_data = []
        for point in c.points:
            cluster_data.append(point.coords)

        trace = {}
        centroid = {}
        if dimensions == 2:
            # Convert our list of x,y's into an x list and a y list.
            trace['x'], trace['y'] = zip(*cluster_data)
            trace['mode'] = 'markers'
            trace['marker'] = {}
            trace['marker']['symbol'] = i
            trace['marker']['size'] = 12
            trace['name'] = "Cluster " + str(i)
            traceList.append(Scatter(**trace))
            # Centroid (A trace of length 1)
            centroid['x'] = [c.centroid.coords[0]]
            centroid['y'] = [c.centroid.coords[1]]
            centroid['mode'] = 'markers'
            centroid['marker'] = {}
            centroid['marker']['symbol'] = i
            centroid['marker']['color'] = 'rgb(200,10,10)'
            centroid['name'] = "Centroid " + str(i)
            traceList.append(Scatter(**centroid))
        else:
            symbols = [
                "circle",
                "square",
                "diamond",
                "circle-open",
                "square-open",
                "diamond-open",
                "cross", "x"
            ]
            symbol_count = len(symbols)
            if i > symbol_count:
                print ("Warning: Not enough marker symbols to go around")
            # Convert our list of x,y,z's separate lists.
            trace['x'], trace['y'], trace['z'] = zip(*cluster_data)
            trace['mode'] = 'markers'
            trace['marker'] = {}
            trace['marker']['symbol'] = symbols[i]
            trace['marker']['size'] = 12
            trace['name'] = "Cluster " + str(i)
            traceList.append(Scatter3d(**trace))
            # Centroid (A trace of length 1)
            centroid['x'] = [c.centroid.coords[0]]
            centroid['y'] = [c.centroid.coords[1]]
            centroid['z'] = [c.centroid.coords[2]]
            centroid['mode'] = 'markers'
            centroid['marker'] = {}
            centroid['marker']['symbol'] = symbols[i]
            centroid['marker']['color'] = 'rgb(200,10,10)'
            centroid['name'] = "Centroid " + str(i)
            traceList.append(Scatter3d(**centroid))

    title = "K-means clustering with %s clusters" % str(len(data))
    plotly.offline.plot({
        "data": traceList,
        "layout": Layout(title=title)
    })

if __name__ == "__main__":
    main()